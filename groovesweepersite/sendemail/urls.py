from django.urls import path
from .views import contactView, successView

urlpatterns = [
	path('contact/', contactView, name = 'contact'),
	path('success/', successView, name = 'success'),
]
