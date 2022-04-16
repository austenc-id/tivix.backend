from django.urls import path, include
from rest_framework.routers import DefaultRouter
from omdb.views import *



primary_router = DefaultRouter()
primary_router.register(r'movies', MovieViewSet)
primary_router.register(r'galleries', GalleryViewSet)
primary_router.register(r'reviews', ReviewViewSet)


supporting_router = DefaultRouter()
supporting_router.register(r'mediums', MediumViewSet)
supporting_router.register(r'genres', GenreViewSet)
supporting_router.register(r'audiences', AudienceViewSet)
supporting_router.register(r'directors', DirectorViewSet)
supporting_router.register(r'writers', WriterViewSet)
supporting_router.register(r'actors', ActorViewSet)
supporting_router.register(r'languages', LanguageViewSet)
urlpatterns = [
    path('api/', include(primary_router.urls)),
    path('api/misc/', include(supporting_router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))
]