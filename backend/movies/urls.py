from django.urls import path

from movies.views import MoviesListView, FavoritesMoviesListView

app_name = 'movies'

urlpatterns = [
    path('search/', MoviesListView.as_view(), name='search-movies'),
    path('favorites-list/', FavoritesMoviesListView.as_view(), name='favorites-movies-list'),
]