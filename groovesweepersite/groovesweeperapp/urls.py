from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('lyrics/', views.lyrics, name='lyrics'),
	path('results/', views.results, name='results'),
]
