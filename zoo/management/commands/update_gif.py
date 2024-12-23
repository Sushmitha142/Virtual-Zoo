from django.core.management.base import BaseCommand
from zoo.models import Animal

class Command(BaseCommand):
    help = "Update the GIF field for Elephant in the Animal model."

    def handle(self, *args, **kwargs):
        try:
            # Fetch the Elephant object by primary key (adjust the pk if necessary)
            elephant = Animal.objects.get(pk=2)
            
            # Update the gif field with the correct file path
            elephant.gif = 'animals_gifs/elephant.gif'  # Relative to MEDIA_ROOT
            
            # Save the changes
            elephant.save()
            
            # Output a success message
            self.stdout.write(self.style.SUCCESS("Successfully updated GIF for Elephant."))
        
        except Animal.DoesNotExist:
            # Handle the case where no matching Animal is found
            self.stdout.write(self.style.ERROR("Animal with pk=2 does not exist. Please check the database."))
        except Exception as e:
            # Handle any unexpected errors
            self.stdout.write(self.style.ERROR(f"An error occurred: {str(e)}"))
