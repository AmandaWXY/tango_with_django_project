from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!")
	return HttpResponse("<a href='/rango/about/'>About</a>")
def about(request):
	return HttpResponse("Rango says here is the about page.")
	return HttpResponse("<a href='/rango/'>Index</a>")