from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('movie/', MovieListView.as_view(), name='Movie_list'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='Movie_detail'),
    path('movie/create/', MovieCreateView.as_view(), name='Movie_create'),
    path('movie/<int:pk>/update/', MovieUpdateView.as_view(), name='Movie_update'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='Movie_delete'),
]