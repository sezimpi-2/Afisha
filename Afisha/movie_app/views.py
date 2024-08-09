from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializer import DirectorSerializer, MovieSerializer, ReviewSerializer

# Create your views here.
@api_view(['GET'])
def director_list_api_view(request):
    director_list = Director.objects.all()
    data = DirectorSerializer(director_list, many=True)
    return Response(data=data.data)

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director_detail = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": " Not Found"})
    data = DirectorSerializer(director_detail)
    return Response(data=data.data)


@api_view(['GET'])
def movie_list_api_view(request):
    movie_list = Movie.objects.all()
    data = MovieSerializer(movie_list, many=True)
    return Response(data=data.data)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": " Movie Not Found"})
    data = MovieSerializer(movie_detail)
    return Response(data=data.data)


@api_view(['GET'])
def review_list_api_view(request):
    review_list = Review.objects.all()
    data = ReviewSerializer(review_list, many=True)
    return Response(data=data.data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Review Not Found"})

    data = ReviewSerializer(review_detail)
    return Response(data=data.data)

# Create your views here.
