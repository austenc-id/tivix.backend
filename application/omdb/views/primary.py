from django.shortcuts import redirect
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from omdb.models import *
from omdb.serializers import *
from .utils import tracker, requester


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [permissions.AllowAny]

    def update(self, request, **kwargs):
        print(request.data)
        gallery = self.get_object()
        try:
            for production in request.data['productions']:
                gallery.productions.add(production)
        except:
            for production in request.data['remove']:
                gallery.productions.remove(production)
        gallery.save()
        serialized = GallerySerializer(gallery, context={'request': request})
        return Response(serialized.data)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Production.objects.filter(medium=1)
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['GET'])
    def query(self, request, pk=None):
        trace = tracker(0)
        try:
            movie = self.get_object()
            trace = tracker(trace)
            return redirect(f'/api/movies/{movie.id}')

        except Exception as e:
            existing = Production.objects.filter(title__contains=pk)
            trace = tracker(trace*10)
            if len(existing) == 0:
                trace = tracker(trace)
                try:
                    omdb_response = requester.movie(pk)
                    trace = tracker(trace)
                    try:
                        trace = tracker(trace)
                        omdb_response['message']
                        return Response({'message': 'Movie not found on OMDb!'})
                    except Exception as e:
                        movie = omdb_response['movie']
                        return redirect(f'/api/movies/{movie.id}')
                except Exception as e:
                    return Response({'message': f'{e}'})
            else:
                movie = existing[0]
                trace = tracker(trace)
                return redirect(f'/api/movies/{movie.id}')

    @action(detail=True, methods=['GET'])
    def details(self, request, pk=None):
        try:
            movie = self.get_object()
            return Response(movie.to_dict())
        except:
            return Response({'message': 'Details not found.'})



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]