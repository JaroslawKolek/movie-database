from rest_framework import serializers

from ..models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'imdb_id')

    def create(self, validated_data):
        movie = Movie.objects.create(
            title=validated_data['title'],
            imdb_id=validated_data['imdb_id'],
        )
        return movie
