from django.urls import path

from .views import MoviesListView, FavoritesMoviesListView

app_name = 'movies'

urlpatterns = [
    path('search/', MoviesListView.as_view(), name='search_movies'),
    path('favorites/', FavoritesMoviesListView.as_view(), name='favorites_movies')
]
