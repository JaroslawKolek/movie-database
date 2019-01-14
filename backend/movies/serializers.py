from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        return obj in user.userdetails.favorites_movies.all()

    class Meta:
        model = Movie
        fields = '__all__'
