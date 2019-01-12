from django.urls import path

from movies.views import MoviesSearchView, FavoritesMoviesListView

app_name = 'movies'

urlpatterns = [
    path('search/', MoviesSearchView.as_view(), name='search-movies'),
    path('favorites-list/', FavoritesMoviesListView.as_view(), name='favorites-movies-list'),
]