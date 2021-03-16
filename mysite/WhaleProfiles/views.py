from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('WhaleProfiles/index.html')
    return HttpResponse("Account Login/Sign Up, Species list to see data for each species. ")

def addSpecie(request):
    template = loader.get_template('WhaleProfiles/addSpecie.html')
    return HttpResponse("Where the user can create new species to add data")

def editSpecie(request):
    template = loader.get_template('WhaleProfiles/editSpecie.html')
    return HttpResponse("Where the user can edit already existing species")

def speciesPage(request):
    template = loader.get_template('WhaleProfiles/speciesPage.html')
    return HttpResponse("Where all the species with their data is displayed")
