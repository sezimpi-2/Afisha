from django.contrib import admin
from django.urls import path
from movie_app.views import (
    director_list_api_view,
    director_detail_api_view,
    movie_list_api_view,
    movie_detail_api_view,
    review_list_api_view,
    review_detail_api_view
)

urlpatterns = [
    # для работы с режиссерами
    path('api/v1/directors/', director_list_api_view, name='director-list'),
    path('api/v1/directors/<int:id>/', director_detail_api_view, name='director-detail'),

    #  для работы с фильмами
    path('api/v1/movies/', movie_list_api_view, name='movie-list'),
    path('api/v1/movies/<int:id>/', movie_detail_api_view, name='movie-detail'),

    # для работы с отзывами
    path('api/v1/reviews/', review_list_api_view, name='review-list'),
    path('api/v1/reviews/<int:id>/', review_detail_api_view, name='review-detail'),
]
