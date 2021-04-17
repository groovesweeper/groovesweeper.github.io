from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import SongQueryForm, FilterForm
from .models import SongQueryModel
from .src.model.Filter import Filter

# Create your views here.
def homeView(request, mod = ""):
	# Home view when you first load the app. This page has a search bar and edit
	# filter abilities
	term_form = SongQueryForm()
	filter = Filter.getInstance()
	filter_form = FilterForm()

	# This if statement is triggered if a button is pressed on the page
	if (request.method == 'POST'):
		# This if statement is if the pressed button is the search button
		if 'search-button' in request.POST:
			term_form = SongQueryForm(request.POST)
			if term_form.is_valid():
				term_form.save()
				query = term_form.cleaned_data['term']
				return HttpResponseRedirect(reverse('results', args=(query,)))
		elif 'add-7' in request.POST:
			for word in filter.getSevenDirtyWords():
				filter.addWord(word)
			mod = "mod"
			return HttpResponseRedirect(reverse('home-mod', args = (mod,)))
		elif 'add-common' in request.POST:
			for word in filter.getCommonSwearWords():
				filter.addWord(word)
			mod = "mod"
			return HttpResponseRedirect(reverse('home-mod', args = (mod,)))
		elif 'add-custom' in request.POST:
			filter_form = FilterForm(request.POST)
			if filter_form.is_valid():
				words_to_add = filter_form.cleaned_data['to_add'].split(",")
				for word in words_to_add:
					filter.addWord(word.strip())
				mod = "mod"
				return HttpResponseRedirect(reverse('home-mod', args = (mod,)))
		else:
			for word in filter.getFullFilter():
				if word in request.POST:
					filter.removeWord(word)
					mod = "mod"
					return HttpResponseRedirect(reverse('home-mod', args = (mod,)))
	context = {
				'term_form':term_form,
				'filter_form':filter_form,
				'7dw':str(filter.getSevenDirtyWords()),
				'common_swears':str(filter.getCommonSwearWords()),
				'full_filter':filter.getFullFilter(),
				'all7':filter.all7(),
				'all_common':filter.allCommon(),
				'start_modal':(mod == "mod")
			  }
	return render(request, 'groovesweeperapp/index.html', context)

def lyricsView(request, song_id):
	return render(request, 'groovesweeperapp/lyrics.html')

def resultsView(request, query):
    return render(request, 'groovesweeperapp/results.html')
