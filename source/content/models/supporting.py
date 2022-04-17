from .__imports import *


class Genre(Model):
    name = TextField()

    def __str__(self):
        return self.name


class GenreSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class GenreViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny]


class Director(Model):
    name = TextField()

    def __str__(self):
        return self.name


class DirectorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['name']


class DirectorViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = [AllowAny]


class Writer(Model):
    name = TextField()

    def __str__(self):
        return self.name


class WriterSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = ['name']


class WriterViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes = [AllowAny]


class Actor(Model):
    name = TextField()

    def __str__(self):
        return self.name


class ActorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['name']


class ActorViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [AllowAny]


class Review(Model):
    production = ForeignKey('Production', on_delete=CASCADE)
    source = TextField()
    score = DecimalField(max_digits=3, decimal_places=1)
    possible = IntegerField()

    def __str__(self):
        return self.movie.title


class ReviewSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewViewSet(ModelViewSet):
    from rest_framework.permissions import AllowAny
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
