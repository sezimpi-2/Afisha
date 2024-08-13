from rest_framework import serializers
from .models import Director, Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return sum(review.stars for review in reviews) / reviews.count()
        return None

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.director.count()
