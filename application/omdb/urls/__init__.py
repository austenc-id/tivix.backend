from django.urls import path, include
from rest_framework.routers import DefaultRouter
from omdb.views import *
from .primary import primary_router
from .supporting import supporting_router






urlpatterns = [
    path('api/', include(primary_router.urls)),
    path('search/movies/<str:query>', search.movies),
    path('api/misc/', include(supporting_router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))
]