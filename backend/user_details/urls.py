from django.urls import path

from user_details.views import LoginView, UserFavouriteMovieManagementView

app_name = 'user_details'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('favorite-movies/', UserFavouriteMovieManagementView.as_view(), name='manage-favorite-movies'),
]
