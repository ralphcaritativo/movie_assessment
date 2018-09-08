from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_movies, name='list_movies'),
    path('detail/<int:id>', views.detail_movies, name='detail_movies'),
    path('create', views.create_movie, name='create_movie'),
    path('update/<int:id>', views.update_movie, name='update_movie'),
    path('delete/<int:id>', views.delete_movie, name='delete_movie'),
    path('like_total/<int:id>', views.like_total, name='like_total'),
]
