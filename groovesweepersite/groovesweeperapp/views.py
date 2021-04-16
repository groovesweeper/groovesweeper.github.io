from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import SongQueryForm
from .models import SongQueryModel
from .src.model.Filter import Filter

# Create your views here.
def homeView(request):
	# Home view when you first load the app. This page has a search bar and edit
	# filter abilities
	term_form = SongQueryForm()
	filter = Filter.getInstance()

	# This if statement is triggered if a button is pressed on the page
	if (request.method == 'POST'):
		# This if statement is if the pressed button is the search button
		if 'search-button' in request.POST:
			term_form = SongQueryForm(request.POST)
			if term_form.is_valid():
				term_form.save()
				query = term_form.cleaned_data['term']
				return HttpResponseRedirect(reverse('results', args=(query,)))
		if 'add7' in request.POST:
			for word in filter.getSevenDirtyWords():
				filter.addWord(word)
			return HttpResponseRedirect(reverse('home'))
		if 'addcommon' in request.POST:
			for word in filter.getCommonSwearWords():
				filter.addWord(word)
			return HttpResponseRedirect(reverse('home'))
	context = {
				'term_form':termform,
				'7dw':str(filter.getSevenDirtyWords()),
				'common_swears':str(filter.getCommonSwearWords()),
				'all7':filter.all7(),
				'all_common':filter.allCommon()
			  }
	return render(request, 'groovesweeperapp/index.html', context)

def lyricsView(request, song_id):
	return render(request, 'groovesweeperapp/lyrics.html')

def resultsView(request, query):
    return render(request, 'groovesweeperapp/results.html')
