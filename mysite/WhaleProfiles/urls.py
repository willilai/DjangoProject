from django.urls import path

from . import views

app_name = 'WhaleProfiles'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('addSpecie/', views.addSpecie, name='addSpecie'),
    path('editSpecie/', views.editSpecie, name='editSpecie'),
]
