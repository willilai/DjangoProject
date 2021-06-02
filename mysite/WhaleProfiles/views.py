from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Specie, Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.views import View

class Index(View):
    # gets all the users, profiles, and species of whales in the database
    allUsers = User.objects.all()
    allProfiles = Profile.objects.all()
    whales = Specie.objects.all()
    def get(self, request):
        # a dictionary that holds all the data necessary for the template
        context = {
        'allUsers': self.allUsers,
        'allProfiles': self.allProfiles,
        'whales': self.whales
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/index.html')
        return HttpResponse(template.render(context, request))
    def post(self, request):
        # if there is post data
        if request.method == "POST":
            # This tests if the form is the log *in* form
            if 'inputUsername' in request.POST.keys():
                # IF so, try to authentircate
                user = authenticate(username=request.POST['inputUsername'],
                    password=request.POST['inputPassword'])
                if user is not None:
                    # IF success, then use the login function so the session persists.
                    login(request, user)
                    if user.is_authenticated:
                        profile = Profile.objects.get(user=user)
                    # a dictionary that holds all the data necessary for the template
                    context = {
                    'allUsers': self.allUsers,
                    'whales': self.whales,
                    'user': user,
                    'profile': profile
                    }
                else:
                    pass
            # This tests if the form is the log *out* form
            elif 'logout' in request.POST.keys():
                # If so, don't need to check anything else, just kill the session.
                logout(request)
        # a dictionary that holds all the data necessary for the template
        context = {
        'allUsers': self.allUsers,
        'allProfiles': self.allProfiles,
        'whales': self.whales
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/index.html')
        return HttpResponse(template.render(context, request))

class AddSpecie(View):
    # gets all the species of whales in the database
    whales = Specie.objects.all()
    def get(self, request):
        # a dictionary that holds all the data necessary for the template
        context = {
        'whales': self.whales,
        'user': request.user
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/addSpecie.html')
        return HttpResponse(template.render(context, request))
    def post(self, request):
        # if there is post data
        if request.method == "POST":
            # assigns the data received to variables
            inputName = request.POST['name']
            inputNumber = request.POST['numWhales']
            inputDiet = request.POST['diet']
            inputSize = request.POST['size']
            inputWeight = request.POST['weight']
        # creates a new species with the data received
        whale = Specie(
            name = inputName,
            numWhales = inputNumber,
            diet = inputDiet,
            size = inputSize,
            weight = inputWeight
        )
        # saves the new specie to the database
        whale.save()
        # a dictionary that holds all the data necessary for the template
        context = {
        'whales': self.whales
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/addSpecie.html')
        return HttpResponse(template.render(context, request))

class EditSpecie(View):
    # gets all the species of whales in the database
    whales = Specie.objects.all()
    def get(self, request):
        # a dictionary that holds all the data necessary for the template
        context = {
                'whales': self.whales,
                'user': request.user
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/editSpecie.html')
        return HttpResponse(template.render(context, request))
    def post(self, request):
        # if there is post data
        if request.method == "POST":
            # assigns the data received to variables
            inputName = request.POST['name']
            inputNumber = request.POST['numWhales']
            inputDiet = request.POST['diet']
            inputSize = request.POST['size']
            inputWeight = request.POST['weight']
        # looks through all the species of whale
        for whale in self.whales:
            # if the name of the whale is the specie the user wants to edit
            if whale.name == inputName:
                # changes the values with the data received from the user
                whale.name = inputName
                whale.numWhales = inputNumber
                whale.diet = inputDiet
                whale.size = inputSize
                whale.weight = inputWeight
            # saves the changes
            whale.save()
        # a dictionary that holds all the data necessary for the template
        context = {
        'whales': self.whales
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/editSpecie.html')
        return HttpResponse(template.render(context, request))

class CreateUser(View):
    # gets all the users and profiles from the database
    allUsers = User.objects.all()
    allProfiles = Profile.objects.all()
    def get(self, request):
        # a dictionary that holds all the data necessary for the template
        context = {
            'allUsers': self.allUsers
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/createUser.html')
        return HttpResponse(template.render(context, request))
    def post(self, request):
        # if there is post data
        if request.method == "POST":
            # assigns the data received to variables to be used later
            inputUsername = request.POST['username']
            inputPassword = request.POST['password']
            inputRole = request.POST['role']
        # creates a new user with the data received
        user = User(
            username = inputUsername,
            password = make_password(inputPassword)
        )
        # saves the new user into the database
        user.save()
        # creates a new profile with the data received
        profile = Profile(
            user = user,
            role = inputRole
        )
        # saves the new profile into the database
        profile.save()
        # a dictionary that holds all the data necessary for the template
        context = {
            'allUsers': self.allUsers,
            'allProfiles': self.allProfiles
        }
        # connects the view with the template and sends the data to the template
        template = loader.get_template('WhaleProfiles/createUser.html')
        return HttpResponse(template.render(context, request))
