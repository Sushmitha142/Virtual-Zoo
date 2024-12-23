from django.shortcuts import redirect, render, get_object_or_404

from zoo.forms import AnimalForm
from .models import Habitat, Animal

def home(request):
    habitats = Habitat.objects.all()
    return render(request, 'zoo/home.html', {'habitats': habitats})

def home(request):
    animals = Animal.objects.all()  # Fetch all animals from the database
    return render(request, 'zoo/home.html', {'animals': animals})

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animal_list')  # Redirect to the animal list page
    else:
        form = AnimalForm()

def animals_list(request):
    animals = Animal.objects.all()  # Query all animals from the database
    return render(request, 'zoo/animals_list.html', {'animals': animals})

def habitat_detail(request, habitat_id):
    habitat = get_object_or_404(Habitat, id=habitat_id)
    return render(request, 'zoo/habitat_detail.html', {'habitat': habitat})

# def animal_detail(request, animal_id):
#     animal = get_object_or_404(Animal, id=animal_id)
#     return render(request, 'zoo/animal_detail.html', {'animal': animal})
def animal_detail(request, pk):
    animal = Animal.objects.get(pk=pk)
    return render(request, 'animal_detail.html', {'animal': animal})

# Create your views here.
def map(request):
    return render(request, 'zoo/map.html')