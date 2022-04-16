from rest_framework.routers import DefaultRouter
from omdb.views import *


primary_router = DefaultRouter()
primary_router.register(r'movies', MovieViewSet)
primary_router.register(r'galleries', GalleryViewSet)
primary_router.register(r'reviews', ReviewViewSet)
primary_router.register(r'searches', SearchViewSet)