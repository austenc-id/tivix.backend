from django.contrib import admin
from django.urls import path, include
from .view import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include('omdb.urls'))
]
