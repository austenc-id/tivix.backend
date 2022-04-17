from .__imports import *

choices = [
    ('default', 'default'),
    ('created', 'created'),
    ('search', 'search')
]
class Gallery(Model):
    class Meta:
        verbose_name_plural = 'Galleries'
    title = TextField(unique=True)
    type = TextField(choices=choices)
    description = TextField()
    productions = ManyToManyField(
    'Production', blank=True, related_name='gallery_productions')
    def movies(self):
        movies = self.productions.filter(type='movie')
        movie_list = []
        for movie in movies:
            movie = {
                'id': movie.id,
                'card': movie.card()
            }
            movie_list.append(movie)
        return movie_list


class Serializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'type','title', 'description', 'movies']


class ViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Gallery.objects.all()
    serializer_class = Serializer
    permission_classes = [AllowAny]

    def update(self, request, **kawrgs):
        from rest_framework.response import Response
        gallery = self.get_object
        try:
            for movie in request.data['add']:
                gallery.productions.add(movie)
        except Exception as E:
            print(E)
        try:
            for movie in request.data['remove']:
                gallery.productions.remove(movie)
        except Exception as E:
            print(E)
        gallery.save()
        gallery = Serializer(gallery, context={'request': request})
        return Response(gallery.data)
