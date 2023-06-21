import json
import os


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch movies from the database
        movies_from_table = Movie.objects.all()
        context['movies_from_table'] = movies_from_table
        
        # Fetch movies from the JSON file
        file_path = os.path.join(os.path.dirname(__file__), 'movies.json')
        with open(file_path) as file:
            movies_from_json = json.load(file)
        context['movies_from_json'] = movies_from_json
        
        return context
        


class MovieDetailView(DetailView):
    template_name = "movie/movie-detail.html"
    model = Movie
    


class MovieCreateView(CreateView):
    template_name = "movie/movie-create.html"
    model = Movie
    fields = ['id','title', 'release_date', 'poster_path', 'overview']
    def form_valid(self, form):
        form.instance.watcher = self.request.user
        return super().form_valid(form)


class MovieUpdateView(UpdateView):
    template_name = "movie/movie-update.html"
    model = Movie
    fields = ['id','title', 'release_date', 'poster_path', 'overview']


class MovieDeleteView(DeleteView):
    template_name = "movie/movie-delete.html"
    model = Movie
    success_url = reverse_lazy("Movie_list")


