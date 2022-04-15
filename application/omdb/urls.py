from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import fetch_data
from .viewsets import ProductionViewSet, GalleryViewSet

router = DefaultRouter()
router.register(r'movies', ProductionViewSet)
router.register(r'galleries', GalleryViewSet)

urlpatterns = [
    path('get/<str:media>/<str:name>', fetch_data),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework'))
]