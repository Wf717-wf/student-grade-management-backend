# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# # from pro01.views import UserTypeViewSet, UserViewSet, book_list
#
#
# router = DefaultRouter()
# # router.register(r'user/user_types', UserTypeViewSet)
# # router.register(r'user/userList', UserViewSet)
#
# urlpatterns = [
#     # path('', include(router.urls)),
#     # path('book', book_list),
#     path('movies/', include("movie.urls", namespace="movie")),
#
#
#
# ]

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pro01/', include('pro01.urls')),
    # path('pro02/',include('pro02.urls'))

    path('score/',include('score.urls'))


]
