from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=256)
    imdb_id = models.CharField(max_length=256, unique=True)
    poster_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
