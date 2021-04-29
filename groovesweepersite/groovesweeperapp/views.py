""" The 'views' module controls what is reactively displayed on the html pages

homeView :
    This is the view  when first arriving on the site. It uses the index.html
    template. It has the mod arg to use when the mod should be opened upon load

    term_form : Form representing main search bar
    filter_form : Form representing buttons on modal
    7dw : string containing seven dirty words
    common_swears : string containing our common swear words
    full_filter : All currently filtered words
    all7 : Checks if 7 dirty words are in filter
    all_common : Checks if common swear words are in filter
    start_modal : Notifies whether to start the modal or not

resultsView :
    The view showing the search results. It uses results.html as a template. It
    also takes care of storing song objects in the DB to use on lyrics

    results_list : the 10 songs from results and all relevant data about them
    query : Search term from home page, also in url

lyricsView :
    The view showing the lyrics of the given song. It uses lyrics.html as the
    template. It pulls information about the song from its DB entry which was
    generated on resultsView

    explicit : String containing all explicit words present
    name : Name of song
    artist : Name of artist
    lyrics : String containing all lyrics
    geniusurl : Link to genius.com lyrics page
    song_status : Bool holding True if song is dirty, False if clean
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms.models import model_to_dict
from .forms import SongQueryForm, FilterForm
from .models import SongModel, SongQueryModel
from .src.model.Filter import Filter
from .src.model.Song import *
import lyricsgenius
import re


# Create your views here.
def homeView(request, mod=''):
    """
    Home view when you first load the app. This page has a search bar and edit
    filter abilities
    Occasionally when a change has been made in the modal, the page is refreshed
    and in this case, it is to the url path /mod. When the url is /mod, the
    edit filter modal opens automatically
    """
    term_form = SongQueryForm()
    filter = Filter.getInstance()
    filter_form = FilterForm()

    # This if statement is triggered if a button is pressed on the page
    if request.method == 'POST':
        if 'search-button' in request.POST:
            # This if statement is if the pressed button is the search button
            term_form = SongQueryForm(request.POST)
            if term_form.is_valid():
                query = term_form.cleaned_data['term']
                return HttpResponseRedirect(reverse('results', args=(query,)))
        elif 'add-7' in request.POST:
            # This is triggerd when adding the seven dirty words
            for word in filter.getSevenDirtyWords():
                filter.addWord(word)
            mod = 'mod'
            return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
        elif 'add-common' in request.POST:
            # This is triggerd when adding the common swear words
            for word in filter.getCommonSwearWords():
                filter.addWord(word)
            mod = 'mod'
            return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
        elif 'add-custom' in request.POST:
            # This is triggerd when adding words from text box
            filter_form = FilterForm(request.POST)
            if filter_form.is_valid():
                words_to_add = filter_form.cleaned_data['to_add'].lower().split(',')
                for word in words_to_add:
                    if word != '':
                        filter.addWord(word.strip().lower())
                mod = 'mod'
                return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
        elif 'clear-all' in request.POST:
            # This is triggered when clearing all the words
            filter.clearAll()
            mod = 'mod'
            return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
        else:
            # This is triggered when removing one of the filtered words
            for word in filter.getFullFilter():
                # find which word was filtered
                if word in request.POST:
                    filter.removeWord(word)
                    mod = 'mod'
                    return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
    context = {
        'term_form': term_form,
        'filter_form': filter_form,
        '7dw': str(filter.getSevenDirtyWords()),
        'common_swears': str(filter.getCommonSwearWords()),
        'full_filter': filter.getFullFilter(),
        'all7': filter.all7(),
        'all_common': filter.allCommon(),
        'start_modal': (mod == 'mod')
    }
    return render(request, 'groovesweeperapp/index.html', context)


def resultsView(request, query):
    """
    resultsView lists the responses from the Genius query
    """
    client_details = dict()
    with open('./groovesweeperapp/src/model/client_details.txt') as f:
        # this loop finds the secret client token from the Genius API
        for line in f:
            (key, val) = line.split(':')
            client_details[key] = val
    genius = lyricsgenius.Genius(client_details['CLIENT_TOKEN'].strip('\n'))

    filter = Filter.getInstance()

    ret = genius.search(query, per_page=10)['hits']
    results_list = [None] * 10
    for i in range(len(ret)):
        for_ret = ret[i]['result']
        lyrics = ''
        try:
            lyrics = genius.lyrics(song_id = for_ret['id'])
        except:
            print(for_ret['full_title'], 'time out')
        if lyrics != '':
            # Here we create the song object, used for its class methods
            result = Song(lyrics,
                    for_ret['primary_artist']['name'], for_ret['full_title'], \
                    for_ret['url'])
            results_list[i] = dict()
            results_list[i]['name'] = result.getName()
            results_list[i]['artist'] = result.getArtist()
            results_list[i]['num_explicit'] = result.getNumOfExplicitWords()
            # This if statement is used to specify css for hovering over the
            # results on the page
            if results_list[i]['num_explicit']:
                results_list[i]['is_explicit'] = 'explicit'
            else:
                results_list[i]['is_explicit'] = 'clean'
            results_list[i]['set_explicit'] = result.getExplicitWords()
            results_list[i]['id'] = for_ret['id']
            results_list[i]['url'] = for_ret['url']
            results_list[i]['index'] = i

            # We save the song as a SongModel to the DB to quickly pull it up
            # on the lyrics page
            song = SongModel.objects.createSong(
                                                results_list[i]['name'],
                                                results_list[i]['artist'],
                                                lyrics,
                                                results_list[i]['set_explicit'],
                                                results_list[i]['url'],
                                                results_list[i]['id']
                                                )
            #song.save()

    context = {'results': results_list, 'query' : query}
    return render(request, 'groovesweeperapp/results.html', context)

def lyricsView(request, song_id):
    """
    lyricsView shows us the specified song's lyrics, disqualifying words
    (if any), and highlights said words in the lyrics themselves
    """
    filter = Filter.getInstance()

    # Pulls song info via SQL
    hits = SongModel.objects.filter(db_song_id = song_id)
    chosenSong = model_to_dict(hits[len(hits)-1])

	# adds format to the lyrics for HTML page
    chosenSong['lyrics'] = chosenSong['lyrics'].replace('\n','<br>')

    if chosenSong['explicit_words'] != 'set()':
        # In this case, there are explicit words in the song, some string
        # parsing must occur
        chosenSong['explicit_words'] = chosenSong['explicit_words'][1:-1]
        chosenSong['explicit_words'] = chosenSong['explicit_words'].split(', ')
        #print(type(chosenSong['explicit_words']))
        song_status = True # True = song is dirty
    else:
        song_status = False # False = song is clean

	# highlighting for the explicit words
    if song_status == True:
        for term in chosenSong['explicit_words']:
            term = term.strip('\'')
            pattern = re.compile(re.escape(term), re.IGNORECASE)
            chosenSong['lyrics'] = pattern.sub('<span style="background-color:red;color:white;"">%s</span>' % term, chosenSong['lyrics'])

    context = {
            'explicit':','.join(chosenSong['explicit_words']),
            'name':chosenSong['name'],
            'artist':chosenSong['artist'],
            'lyrics':chosenSong['lyrics'],
            'geniusurl':chosenSong['url'],
			'song_status': song_status

        }
    return render(request, 'groovesweeperapp/lyrics.html', context)
