from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=256)


class Production(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    language = models.CharField(max_length=120, blank=True)
    runtime = models.CharField(max_length=50, blank=True)
    release_date = models.DateField()
    poster_url = models.CharField(max_length=256, blank=True)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    production = models.ForeignKey(Production, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
