from content.models.supporting import GenreViewSet, DirectorViewSet, WriterViewSet, ActorViewSet, ReviewViewSet
from rest_framework.routers import DefaultRouter

supporting = DefaultRouter()
supporting.register(r'genres', GenreViewSet)
supporting.register(r'directors', DirectorViewSet)
supporting.register(r'writers', WriterViewSet)
supporting.register(r'actors', ActorViewSet)
supporting.register(r'reviews', ReviewViewSet)