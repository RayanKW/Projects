from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# Create your views here.


def home(request):
    # return HttpResponse('<h1>hey there</h1>')
    searchTerm = request.GET.get('searchMovie')
    movies = Movie.objects.all()
    context = {
        'searchTerm': searchTerm, 'movies':movies
    }#incase of two items to be rendered use a dictionary
    return render(request, 'home.html', context)


def about(request):
    return HttpResponse('<h2>This is the about page</h2>')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
