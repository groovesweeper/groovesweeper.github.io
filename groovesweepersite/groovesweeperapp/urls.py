from django.urls import path
from . import views

urlpatterns = [
	path('', views.homeView, name = 'home'),
	path('lyrics/', views.lyricsView, name = 'lyrics'),
	path('results/', views.resultsView, name = 'results'),
]
