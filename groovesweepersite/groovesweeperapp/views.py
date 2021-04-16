from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import SongQueryForm
from .models import SongQueryModel

# Create your views here.
def homeView(request):
	form = SongQueryForm()

	if (request.method == 'POST'):
		form = SongQueryForm(request.POST)
		if form.is_valid():
			form.save()
			query = form.cleaned_data['term']
			return HttpResponseRedirect(reverse('results', args=(query,)))
	context = {'form':form}
	return render(request, 'groovesweeperapp/index.html', context)

def lyricsView(request, song_id):
	return render(request, 'groovesweeperapp/lyrics.html')

def resultsView(request, query):
    return render(request, 'groovesweeperapp/results.html')
