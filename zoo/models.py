from django.db import models

class Habitat(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    habitat = models.ForeignKey(Habitat, on_delete=models.CASCADE, null=True, blank=True)
    diet = models.CharField(max_length=100)
    description = models.TextField()
    gif = models.ImageField(upload_to='animals_gifs/', null=True, blank=True)
    

    def __str__(self):
        return self.name
