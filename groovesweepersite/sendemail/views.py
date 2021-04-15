from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def contactView(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['admin@example.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "sendemail/email.html", {'form' : form})

def successView(request):
	return HttpResponse('Successfully sent! Thank you for your message. We will contact you shortly.')
