from django.core.management.base import BaseCommand
from zoo.models import Animal

class Command(BaseCommand):
    help = "Update GIF field for Elephant"

    def handle(self, *args, **kwargs):
        try:
            elephant = Animal.objects.get(pk=2)
            elephant.gif = 'animals_gifs/elephant.gif'
            elephant.save()
            self.stdout.write(self.style.SUCCESS("Successfully updated GIF for Elephant."))
        except Animal.DoesNotExist:
            self.stdout.write(self.style.ERROR("Animal with PK=2 does not exist."))
