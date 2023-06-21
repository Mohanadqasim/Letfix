from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Movie


class MovieListView(ListView):
    template_name = "movie/movie-list.html"
    model = Movie


class MovieDetailView(DetailView):
    template_name = "movie/movie-detail.html"
    model = Movie


class MovieCreateView(CreateView):
    template_name = "movie/movie-create.html"
    model = Movie
    fields = ['title', 'release_date', 'poster_path', 'overview']


class MovieUpdateView(UpdateView):
    template_name = "movie/movie-update.html"
    model = Movie
    fields = []


class MovieDeleteView(DeleteView):
    template_name = "movie/movie-delete.html"
    model = Movie
    success_url = reverse_lazy("_list")