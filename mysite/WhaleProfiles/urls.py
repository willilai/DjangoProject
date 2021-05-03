from django.urls import path

from . import views

app_name = 'WhaleProfiles'
urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('addSpecie/', views.AddSpecie.as_view(), name='addSpecie'),
    path('editSpecie/', views.EditSpecie.as_view(), name='editSpecie'),
    path('createUser/', views.CreateUser.as_view(), name='createUser')
]
