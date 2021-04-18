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
def homeView(request, mod=""):
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
    if (request.method == 'POST'):
        if 'search-button' in request.POST:
            # This if statement is if the pressed button is the search button
            term_form = SongQueryForm(request.POST)
            if term_form.is_valid():
                # term_form.save()
                query = term_form.cleaned_data['term']
                return HttpResponseRedirect(reverse('results', args=(query,)))
        elif 'add-7' in request.POST:
            # This is triggerd when adding the seven dirty words
            for word in filter.getSevenDirtyWords():
                filter.addWord(word)
            mod = "mod"
            return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
        elif 'add-common' in request.POST:
            # This is triggerd when adding the common swear words
            for word in filter.getCommonSwearWords():
                filter.addWord(word)
            mod = "mod"
            return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
        elif 'add-custom' in request.POST:
            # This is triggerd when adding words from text box
            filter_form = FilterForm(request.POST)
            if filter_form.is_valid():
                words_to_add = filter_form.cleaned_data['to_add'].lower().split(",")
                for word in words_to_add:
                    if word != "":
                        filter.addWord(word.strip().lower())
                mod = "mod"
                return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
        else:
            # This is triggered when removing one of the filtered words
            for word in filter.getFullFilter():
                # find which word was filtered
                if word in request.POST:
                    filter.removeWord(word)
                    mod = "mod"
                    return HttpResponseRedirect(reverse('home-mod', args=(mod,)))
    context = {
        'term_form': term_form,
        'filter_form': filter_form,
        '7dw': str(filter.getSevenDirtyWords()),
        'common_swears': str(filter.getCommonSwearWords()),
        'full_filter': filter.getFullFilter(),
        'all7': filter.all7(),
        'all_common': filter.allCommon(),
        'start_modal': (mod == "mod")
    }
    return render(request, 'groovesweeperapp/index.html', context)


def resultsView(request, query, page=1):
	page = int(page) - 1
	client_details = dict()
	with open("./groovesweeperapp/src/model/client_details.txt") as f:
		for line in f:
			(key, val) = line.split(":")
			client_details[key] = val
	genius = lyricsgenius.Genius(client_details["CLIENT_TOKEN"].strip('\n'))

	filter = Filter.getInstance()

	ret = genius.search(query, per_page=50)['hits']
	results_list = [None] * 20
	for i in range(len(ret)):
		for_ret = ret[i]['result']
		lyrics = ""
		try:
			lyrics = genius.lyrics(song_id = for_ret['id'])
		except:
			print(for_ret['full_title'], "time out")
		if lyrics != "":
			result = Song(lyrics,
	      				for_ret['primary_artist']['name'], for_ret['full_title'], for_ret['url'])
			results_list[i] = dict()
			results_list[i]['name'] = result.getName()
			results_list[i]['artist'] = result.getArtist()
			results_list[i]['num_explicit'] = result.getNumOfExplicitWords()
			results_list[i]['set_explicit'] = result.getExplicitWords()
			results_list[i]['id'] = for_ret['id']
			results_list[i]['url'] = for_ret
			results_list[i]['index'] = i

			song = SongModel.objects.createSong(
												results_list[i]['name'],
												results_list[i]['artist'],
												lyrics,
												results_list[i]['set_explicit'],
												results_list[i]['url'],
												results_list[i]['id']
			)
			song.save()

	if (request.method == "POST"):
		info = results_list[int(request.POST['index'])]
		song = SongModel.objects.createSong(
											info['name'],
											info['artist'],
											'fuck you, piss shit',
											",".join(info['set_explicit']),
											"http://google.net",
											str(info['id'])
										  )
		return HttpResponseRedirect(reverse('lyrics', args=(song_id,)))

	context = {'results': results_list, 'query' : query}
	return render(request, 'groovesweeperapp/results.html', context)

def lyricsView(request, song_id):
    filter = Filter.getInstance()

    hits = SongModel.objects.filter(db_song_id = song_id)
    chosenSong = model_to_dict(hits[len(hits)-1])

	# adds format to the lyrics for HTML page
    chosenSong['lyrics'] = chosenSong['lyrics'].replace('\n','<br>')

    if chosenSong['explicit_words'] != 'set()':
        song_status = "EXPLICIT"
    else:
        song_status = "CLEAN"

	# highlighting for the explicit words
    for term in chosenSong['explicit_words'].strip('{}').split(", "):
        term = term.strip('\'')
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        chosenSong['lyrics'] = pattern.sub("<span style='background-color:red;color:white;'>%s</span>" % term, chosenSong['lyrics'])

    context = {
            'explicit':chosenSong['explicit_words'].split(","),
            'name':chosenSong['name'],
            'artist':chosenSong['artist'],
            'lyrics':chosenSong['lyrics'],
            'geniusurl':chosenSong['url'],
			'song_status': song_status
        }

    return render(request, 'groovesweeperapp/lyrics.html', context)
