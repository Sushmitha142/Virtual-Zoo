from django.db import migrations
from django.core.files import File
from zoo.models import Animal, Habitat
import os

def populate_animals(apps, schema_editor):
    # Get the first habitat in the database
    habitat_instance = Habitat.objects.first()  # You can choose a specific habitat if needed
    
    # Check if a habitat is found
    if  habitat_instance:
        # Example data for animals (replace with your own data)
        animal_data = [
        {"name": "Lion", "image_path": "lion.gif"},
        {"name": "Elephant", "image_path": "elephant.gif"},
        {"name": "Giraffe", "image_path": "giraffe.gif"},
        {"name": "Zebra", "image_path": "zebra.gif"},
        {"name": "Kangaroo", "image_path": "kangaroo.gif"},
        {"name": "Panda", "image_path": "panda.gif"},
        {"name": "Tiger", "image_path": "tiger.gif"},
        {"name": "Koala", "image_path": "koala.gif"},
        {"name": "Penguin", "image_path":"penguin.gif"},
        {"name": "Gorilla", "image_path": "gorilla.gif"},
        {"name": "Cheetah", "image_path": "cheetah.gif"},
        {"name": "Rhinoceros", "image_path": "rhinoceros.gif"},
        {"name": "Sloth", "image_path": "sloth.gif"},
        {"name": "Hippopotamus", "image_path": "hippo.gif"},
        {"name": "Jaguar", "image_path": "jaguar.gif"},
        {"name": "Wolf", "image_path": "wolf.gif"},
        {"name": "Owl", "image_path": "owl.gif"},
        {"name": "Polar Bear", "image_path": "polar bear.gif"},
        {"name": "Lemur", "image_path": "lemur.gif"},
        {"name": "Chimpanzee", "image_path": "chimpanzee.gif"}
    ]

    # Iterate over the animal data to save each animal's GIF
    lion = Animal.objects.get(name="Lion")
    if os.path.exists("lion.gif"):
        with open("lion.gif", 'rb') as img_file:
            lion.image.save('Lion.gif', File(img_file), save=False)
            lion.save()
            print("GIF image for Lion has been saved.")
    else:
        print("Gif file for Lion not found: lion.gif")

    # Save Elephant's GIF
    elephant = Animal.objects.get(name="Elephant")
    if os.path.exists("elephant.gif"):
        with open("elephant.gif", 'rb') as img_file:
            elephant.image.save('Elephant.gif', File(img_file), save=False)
            elephant.save()
            print("GIF image for Elephant has been saved.")
    else:
        print("Gif file for Elephant not found: elephant.gif")

    # Save Giraffe's GIF
    giraffe = Animal.objects.get(name="Giraffe")
    if os.path.exists("giraffe.gif"):
        with open("giraffe.gif", 'rb') as img_file:
            giraffe.image.save('Giraffe.gif', File(img_file), save=False)
            giraffe.save()
            print("GIF image for Giraffe has been saved.")
    else:
        print("Gif file for Giraffe not found: giraffe.gif")

    # Save Zebra's GIF
    zebra = Animal.objects.get(name="Zebra")
    if os.path.exists("zebra.gif"):
        with open("zebra.gif", 'rb') as img_file:
            zebra.image.save('Zebra.gif', File(img_file), save=False)
            zebra.save()
            print("GIF image for Zebra has been saved.")
    else:
        print("Gif file for Zebra not found: zebra.gif")

    # Save Kangaroo's GIF
    kangaroo = Animal.objects.get(name="Kangaroo")
    if os.path.exists("kangaroo.gif"):
        with open("kangaroo.gif", 'rb') as img_file:
            kangaroo.image.save('Kangaroo.gif', File(img_file), save=False)
            kangaroo.save()
            print("GIF image for Kangaroo has been saved.")
    else:
        print("Gif file for Kangaroo not found: kangaroo.gif")

    # Save Panda's GIF
    panda = Animal.objects.get(name="Panda")
    if os.path.exists("panda.gif"):
        with open("panda.gif", 'rb') as img_file:
            panda.image.save('Panda.gif', File(img_file), save=False)
            panda.save()
            print("GIF image for Panda has been saved.")
    else:
        print("Gif file for Panda not found: panda.gif")

    # Save Tiger's GIF
    tiger = Animal.objects.get(name="Tiger")
    if os.path.exists("tiger.gif"):
        with open("tiger.gif", 'rb') as img_file:
            tiger.image.save('Tiger.gif', File(img_file), save=False)
            tiger.save()
            print("GIF image for Tiger has been saved.")
    else:
        print("Gif file for Tiger not found: tiger.gif")

    # Save Koala's GIF
    koala = Animal.objects.get(name="Koala")
    if os.path.exists("koala.gif"):
        with open("koala.gif", 'rb') as img_file:
            koala.image.save('Koala.gif', File(img_file), save=False)
            koala.save()
            print("GIF image for Koala has been saved.")
    else:
        print("Gif file for Koala not found: koala.gif")

    # Save Penguin's GIF
    penguin = Animal.objects.get(name="Penguin")
    if os.path.exists("penguin.gif"):
        with open("penguin.gif", 'rb') as img_file:
            penguin.image.save('Penguin.gif', File(img_file), save=False)
            penguin.save()
            print("GIF image for Penguin has been saved.")
    else:
        print("Gif file for Penguin not found: penguin.gif")

    # Save Gorilla's GIF
    gorilla = Animal.objects.get(name="Gorilla")
    if os.path.exists("gorilla.gif"):
        with open("gorilla.gif", 'rb') as img_file:
            gorilla.image.save('Gorilla.gif', File(img_file), save=False)
            gorilla.save()
            print("GIF image for Gorilla has been saved.")
    else:
        print("Gif file for Gorilla not found: gorilla.gif")

    # Save Cheetah's GIF
    cheetah = Animal.objects.get(name="Cheetah")
    if os.path.exists("cheetah.gif"):
        with open("cheetah.gif", 'rb') as img_file:
            cheetah.image.save('Cheetah.gif', File(img_file), save=False)
            cheetah.save()
            print("GIF image for Cheetah has been saved.")
    else:
        print("Gif file for Cheetah not found: cheetah.gif")

    # Save Rhinoceros' GIF
    rhinoceros = Animal.objects.get(name="Rhinoceros")
    if os.path.exists("rhinoceros.gif"):
        with open("rhinoceros.gif", 'rb') as img_file:
            rhinoceros.image.save('Rhinoceros.gif', File(img_file), save=False)
            rhinoceros.save()
            print("GIF image for Rhinoceros has been saved.")
    else:
        print("Gif file for Rhinoceros not found: rhinoceros.gif")

    # Save Sloth's GIF
    sloth = Animal.objects.get(name="Sloth")
    if os.path.exists("sloth.gif"):
        with open("sloth.gif", 'rb') as img_file:
            sloth.image.save('Sloth.gif', File(img_file), save=False)
            sloth.save()
            print("GIF image for Sloth has been saved.")
    else:
        print("Gif file for Sloth not found: sloth.gif")

    # Save Hippopotamus' GIF
    hippopotamus = Animal.objects.get(name="Hippopotamus")
    if os.path.exists("hippo.gif"):
        with open("hippo.gif", 'rb') as img_file:
            hippopotamus.image.save('Hippopotamus.gif', File(img_file), save=False)
            hippopotamus.save()
            print("GIF image for Hippopotamus has been saved.")
    else:
        print("Gif file for Hippopotamus not found: hippopotamus.gif")

    # Save Jaguar's GIF
    jaguar = Animal.objects.get(name="Jaguar")
    if os.path.exists("jaguar.gif"):
        with open("jaguar.gif", 'rb') as img_file:
            jaguar.image.save('Jaguar.gif', File(img_file), save=False)
            jaguar.save()
            print("GIF image for Jaguar has been saved.")
    else:
        print("Gif file for Jaguar not found: jaguar.gif")

    # Save Wolf's GIF
    wolf = Animal.objects.get(name="Wolf")
    if os.path.exists("wolf.gif"):
        with open("wolf.gif", 'rb') as img_file:
            wolf.image.save('Wolf.gif', File(img_file), save=False)
            wolf.save()
            print("GIF image for Wolf has been saved.")
    else:
        print("Gif file for Wolf not found: wolf.gif")

    # Save Owl's GIF
    owl = Animal.objects.get(name="Owl")
    if os.path.exists("owl.gif"):
        with open("owl.gif", 'rb') as img_file:
            owl.image.save('Owl.gif', File(img_file), save=False)
            owl.save()
            print("GIF image for Owl has been saved.")
    else:
        print("Gif file for Owl not found: owl.gif")

    # Save Polar Bear's GIF
    polar_bear = Animal.objects.get(name="Polar Bear")
    if os.path.exists("polar bear.gif"):
        with open("polar bear.gif", 'rb') as img_file:
            polar_bear.image.save('Polar Bear.gif', File(img_file), save=False)
            polar_bear.save()
            print("GIF image for Polar Bear has been saved.")
    else:
        print("Gif file for Polar Bear not found: polar_bear.gif")

    # Save Lemur's GIF
    lemur = Animal.objects.get(name="Lemur")
    if os.path.exists("lemur.gif"):
        with open("lemur.gif", 'rb') as img_file:
            lemur.image.save('Lemur.gif', File(img_file), save=False)
            lemur.save()
            print("GIF image for Lemur has been saved.")
    else:
        print("Gif file for Lemur not found: lemur.gif")

    # Save Chimpanzee's GIF
    chimpanzee = Animal.objects.get(name="Chimpanzee")
    if os.path.exists("chimpanzee.gif"):
        with open("chimpanzee.gif", 'rb') as img_file:
            chimpanzee.image.save('Chimpanzee.gif', File(img_file), save=False)
            chimpanzee.save()
            print("GIF image for Chimpanzee has been saved.")
    else:
        print("Gif file for Chimpanzee not found: chimpanzee.gif")
                        
        
class Migration(migrations.Migration):
        dependencies = [
            ('zoo', '0002_animal_gif_alter_habitat_name'),  # Replace with your actual dependency
        ]

        operations = [
            migrations.RunPython(populate_animals),
        ]
