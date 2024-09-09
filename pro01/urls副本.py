# books/urls.py
from django.urls import path
from .views import author_list, author_detail, author_create, author_update, author_delete,getUser,addUser

urlpatterns = [
    path('authors/', author_list, name='author-list'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
    path('authors/new/', author_create, name='author-create'),
    path('authors/<int:pk>/edit/', author_update, name='author-update'),
    path('authors/<int:pk>/delete/', author_delete, name='author-delete'),

    path('authors/user',getUser,name="user"),

    path('authors/addUser',addUser,name="addUser")
]
