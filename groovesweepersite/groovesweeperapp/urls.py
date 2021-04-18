from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
	path('', views.homeView, name = 'home'),
	path('<mod>', views.homeView, name = 'home-mod'),
	path('<song_id>/lyrics/', views.lyricsView, name = 'lyrics'),
	path('<query>/results/', views.resultsView, name='results'),
	path('<query>/results/<page>', views.resultsView, name='results-page'),
]
