from rest_framework import serializers
from .models import Director, Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    # Валидация для поля stars (1-5)
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5 stars.")
        return value

    # Общая валидация
    def validate(self, data):
        if not data.get('text'):
            raise serializers.ValidationError("Review text is required.")
        return data

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    # Валидация для поля duration (не может быть пустым)
    def validate_duration(self, value):
        if not value:
            raise serializers.ValidationError("Duration is required.")
        return value

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return sum(review.stars for review in reviews) / reviews.count()
        return None

    # Общая валидация
    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError("Title is required.")
        if not data.get('director'):
            raise serializers.ValidationError("Movie must have a director.")
        return data

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    # Валидация для имени режиссера (не может быть пустым)
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Director name cannot be empty.")
        return value

    def get_movies_count(self, obj):
        return obj.movies.count()
