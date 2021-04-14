from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, 'groovesweeperapp/index.html')

def contact(request):
	return render(request, 'groovesweeperapp/contact.html')

def lyrics(request):
	return render(request, 'groovesweeperapp/lyrics.html')
	
