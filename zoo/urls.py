from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('habitat/<int:habitat_id>/', views.habitat_detail, name='habitat_detail'),
    path('animal/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('map/', views.map, name='map'),
    path('animals/', views.animals_list, name='animals_list'),
    path('add-animal/', views.add_animal, name='add_animal'),
     path('animal/<int:pk>/', views.animal_detail, name='animal_detail')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)