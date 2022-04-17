from django.core.management.base import BaseCommand, CommandError
from content.models import Gallery, Production

class Command(BaseCommand):
    help = 'Creates default galleries.'

    def handle(self, *args, **options):
        galleries = ['all productions', 'all movies']
        for gallery in galleries:
            if gallery == 'all productions':
                productions = Production.objects.all()
            elif gallery == 'all movies':
                productions = Production.objects.filter(type='movie')

            gallery = Gallery.objects.get_or_create(title=gallery, description=gallery, type='default')
            gallery = gallery[0]
            for production in productions:
                gallery.productions.add(production)
            gallery.save()