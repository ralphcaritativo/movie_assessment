from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def list_movies(request):
    movies = Movie.objects.all().filter(is_active=1).order_by('title')

    return render(request, 'movies/list_movies.html', {'movies': movies})


def detail_movies(request, id):
    movies = Movie.objects.get(id=id)

    return render(request, 'movies/detail_movies.html', {'movies': movies})


def create_movie(request):
    form = MovieForm(request.POST or None)
    movie = Movie.objects.all()
    if form.is_valid():
        form.save()
        last_saved = Movie.objects.latest('created_at')
        messages.success(request, "{} successfully created!".format(last_saved))
        return render(request, 'movies/detail_movies.html', {'movie':movie})


    return render(request, 'movies/create_movie.html', {'form': form})


def update_movie(request, id):
    movie = Movie.objects.get(id = id)
    form = MovieForm(request.POST or None, instance = movie)

    if form.is_valid():
        form.save()
        messages.success(request, "{} successfully updated".format(movie.title))
        return render(request, 'movies/detail_movies.html', {'movie':movie})

    return render(request, 'movies/create_movie.html', {'form': form, 'movie':movie})


def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        movie.is_active = 0
        movie.save()
        return redirect('list_movies')
        # return render(request, 'movies/list_movies.html', {'movie': movie})



def like_total(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        movie.like_total += 1
        movie.save()
        return redirect('list_movies')
        # return redirect('list_movies', +str(movie.id))
