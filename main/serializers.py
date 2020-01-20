from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Aktor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']


class AktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aktor
        fields = ['imie', 'nazwisko']


class MovieSerializer(serializers.ModelSerializer):
    actors = AktorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'year', 'released', 'actors']




