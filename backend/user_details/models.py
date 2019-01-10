from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    """
    Model extends default User Django model by OneToOneField
    to store more information about user.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites_movies = models.ManyToManyField('movies.Movie')

    def __str__(self):
        return str(self.user)
