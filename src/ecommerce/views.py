from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .forms import ContactForm

from django.contrib.auth import authenticate, login, get_user_model


def home_page(request):
	# print(request.session.get('first_name', 'Unknow'),)
	context = {
		# "title" : "Hello World",
		# "content" : "Welcome to the homepage!",
	}
	if request.user.is_authenticated():
		context["premium_content"] = "Welcome back " + request.user.email
	return render(request, "home_page.html", context)
def about_page(request):
	context = {
		"title" : "About Page",
		"content" : "Please Leave Your Message!"
	}
	return render(request, "home_page.html", context)
def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title" : "Contact",
		"content" : "Welcome to the contact page!",
		"form" : contact_form
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
		if request.is_ajax():
			return JsonResponse({"message": "Thank you for your submission"})

	if contact_form.errors:
		errors = contact_form.errors.as_json()
		if request.is_ajax():
			return HttpResponse(errors, status=400, content_type='application/json')		
	return render(request, "contact/view.html", context)
