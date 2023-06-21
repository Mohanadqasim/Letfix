from django.contrib import admin
from .models import Movie

class CustomMovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ['title', 'release_date', 'poster_path', 'overview']
    fieldsets = (
        ('Owner', {
            'fields': ('watcher',)  # Enclose in a tuple
        }),
        ('Movie_info', {
            'fields': ('id', 'title', 'release_date', 'poster_path', 'overview',)
        }),
    )

admin.site.register(Movie, CustomMovieAdmin)
