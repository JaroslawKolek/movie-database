from rest_framework import serializers

from movies.models import Movie, Director, Production


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production


class MovieSerializer(serializers.ModelSerializer):
    production = serializers.StringRelatedField()
    director = serializers.StringRelatedField()

    class Meta:
        model = Movie
