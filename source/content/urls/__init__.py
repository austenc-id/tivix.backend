from django.urls import path, include
from rest_framework.routers import DefaultRouter
from content.models import Galleries, Productions
from content.views import search


router = DefaultRouter()
router.register(r'galleries', Galleries.ViewSet)
router.register(r'productions', Productions.ViewSet)


app_name = 'content'
urlpatterns = [
    path('api/', include(router.urls), name='api'),
    path('search/<str:query>/<int:quantity>', search, name='search')
]
