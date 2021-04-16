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
	form = SongQueryForm()
	filter = Filter.getInstance()

	# This if statement is triggered if a button is pressed on the page
	if (request.method == 'POST'):
		# This if statement is if the pressed button is the search button
		if 'search-button' in request.POST:
			form = SongQueryForm(request.POST)
			if form.is_valid():
				form.save()
				query = form.cleaned_data['term']
				return HttpResponseRedirect(reverse('results', args=(query,)))
	context = {'form':form, '7dw':str(filter.getSevenDirtyWords())}
	return render(request, 'groovesweeperapp/index.html', context)

def lyricsView(request, song_id):
	return render(request, 'groovesweeperapp/lyrics.html')

def resultsView(request, query):
    return render(request, 'groovesweeperapp/results.html')
