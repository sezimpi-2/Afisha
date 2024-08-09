from django.contrib import admin
from django.urls import path
from Afisha.movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', director_list_api_view),
    path('api/v1/directors/int:id/', director_list_api_view),
    path('api/v1/movies/', movie_list_api_view),
    path('api/v1/movies/int:id/', movie_list_api_view),
    path('api/v1/rewiews/', review_list_api_view),
    path('api/v1/rewiews/int:id', review_list_api_view),
    ]
