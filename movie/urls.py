from django.urls import path
from . import views

# 应用命名空间
app_name = 'movie'

urlpatterns = [
    path('list/', views.movie_list, name='list'),
]
