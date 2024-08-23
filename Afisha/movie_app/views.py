from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializer import DirectorSerializer, MovieSerializer, ReviewSerializer


# Directors
@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        director_list = Director.objects.all()
        data = DirectorSerializer(director_list, many=True).data
        return Response(data=data)

    if request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director_detail = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Director Not Found"})

    if request.method == 'GET':
        data = DirectorSerializer(director_detail).data
        return Response(data=data)

    if request.method == 'PUT':
        serializer = DirectorSerializer(director_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        director_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Movies
@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        movie_list = Movie.objects.all()
        data = MovieSerializer(movie_list, many=True).data
        return Response(data=data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_api_view(request, id):
    try:
        movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Movie Not Found"})

    if request.method == 'GET':
        data = MovieSerializer(movie_detail).data
        return Response(data=data)

    if request.method == 'PUT':
        serializer = MovieSerializer(movie_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Reviews
@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review_list = Review.objects.all()
        data = ReviewSerializer(review_list, many=True).data
        return Response(data=data)

    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Review Not Found"})

    if request.method == 'GET':
        data = ReviewSerializer(review_detail).data
        return Response(data=data)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
