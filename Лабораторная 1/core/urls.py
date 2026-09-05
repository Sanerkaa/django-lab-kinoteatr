from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/add/', views.MovieCreateView.as_view(), name='movie_create'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
]
