from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Virtual Zoo!")
def map_view(request):
    return HttpResponse("This is the map view of the Virtual Zoo.")