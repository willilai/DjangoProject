from django.urls import path

from . import views

app_name = 'WhaleProfiles'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('addSpecie/', views.AddSpecie.as_view(), name='addSpecie'),
    path('editSpecie/', views.EditSpecie.as_view(), name='editSpecie'),
]
