from django.urls import path

from .views import MoviesView, FavoritesMoviesView

app_name = 'movies'

urlpatterns = [
    path('search/', MoviesView.as_view(), name='search_movies'),
    path('favorites/', FavoritesMoviesView.as_view(), name='favorites_movies')
]
