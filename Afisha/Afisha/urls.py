from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from movie_app.views import (
    DirectorListCreateAPIView,
    DirectorRetrieveUpdateDestroyAPIView,
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Directors
    path('directors/', DirectorListCreateAPIView.as_view(), name='director-list-create'),
    path('directors/<int:id>/', DirectorRetrieveUpdateDestroyAPIView.as_view(), name='director-detail'),

    # Movies
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:id>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),

    # Reviews
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:id>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
]

