from django.urls import path

from user_details.views import LoginView, UserFavouriteMovieManagementView, LogoutView

app_name = 'user_details'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('favorite-movies/', UserFavouriteMovieManagementView.as_view(), name='manage-favorite-movies'),
]
