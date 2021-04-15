from django.shortcuts import render
from django.http import HttpResponse
from .forms import SongQueryForm
import lyricsgenius

# Create your views here.
def homeView(request):
	form = SongQueryForm()

	if (request.method == 'POST'):
		form = SongQueryForm(request.POST)
		if form.is_valid():
			client_details = {}
			with open("groovesweeperapp/src/model/client_details.txt") as f:
				for line in f:
					(key, val) = line.split(":")
					client_details[key] = val

			genius = lyricsgenius.Genius(client_details["CLIENT_TOKEN"])
			hit = genius.search(form.cleaned_data['term'], per_page=50)['hits'][0]['result']['id']
			genius.lyrics(song_id=hit)
	context = {'form':form}
	return render(request, 'groovesweeperapp/index.html', context)

def lyricsView(request):
	return render(request, 'groovesweeperapp/lyrics.html')

def resultsView(request):
    return render(request, 'groovesweeperapp/results.html')
