from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_favourite_movies = self.context['request'].user.userdetails\
            .favorites_movies.all().values_list('id', flat=True)

    is_favorite = serializers.SerializerMethodField()

    def get_is_favorite(self, obj):
        return obj.id in self.user_favourite_movies

    class Meta:
        model = Movie
        fields = '__all__'
