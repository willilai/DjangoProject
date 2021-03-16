from django.urls import path

from . import views

app_name = 'WhaleProfiles'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.addSpecie, name='addSpecie'),
    path('', views.editSpecie, name='editSpecie'),
    path('', views.speciesPage, name='speciesPage')
]
