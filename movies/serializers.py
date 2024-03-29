from rest_framework import serializers
from .models import Ratings, Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=Ratings.choices,
        default=Ratings.G,
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie) -> str:
        return obj.user.email

    def create(self, validated_data: dict) -> Movie:
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)

    title = serializers.SerializerMethodField()
    buyed_by = serializers.SerializerMethodField()

    def get_title(self, obj: MovieOrder) -> str:
        return obj.movie.title

    def get_buyed_by(self, obj: MovieOrder) -> str:
        return obj.buyer.email

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)
