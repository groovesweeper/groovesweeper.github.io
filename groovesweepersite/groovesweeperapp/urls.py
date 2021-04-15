from django.urls import path
from . import views

urlpatterns = [
	path('', views.homeView, name = 'home'),
	path('<song_id>/', views.lyricsView, name = 'lyrics'),
	path('<query>/results/', views.resultsView, name = 'results'),
]
