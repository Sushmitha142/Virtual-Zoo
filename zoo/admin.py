from django.contrib import admin
from .models import Habitat, Animal



@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'habitat']