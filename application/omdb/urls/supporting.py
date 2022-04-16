from rest_framework.routers import DefaultRouter
from omdb.views import *


supporting_router = DefaultRouter()
supporting_router.register(r'mediums', MediumViewSet)
supporting_router.register(r'genres', GenreViewSet)
supporting_router.register(r'audiences', AudienceViewSet)
supporting_router.register(r'directors', DirectorViewSet)
supporting_router.register(r'writers', WriterViewSet)
supporting_router.register(r'actors', ActorViewSet)
supporting_router.register(r'languages', LanguageViewSet)