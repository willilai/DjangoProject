from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Specie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.POST:
        # This tests if the form is the log *in* form
        if 'inputUsername' in request.POST.keys():
            # IF so, try to authentircate
            user = authenticate(username=request.POST['inputUsername'],
                password=request.POST['inputPassword'])
            if user is not None:
                # IF success, then use the login function so the session persists.
                login(request, user)
            else:
                pass
                # Message for failed login.
        # This tests if the form is the log *out* form
        elif 'logout' in request.POST.keys():
            # If so, don't need to check anything else, just kill the session.
            logout(request)
    # After we check the forms, set a flag for use in the template.
    if request.user.is_authenticated:
        loggedIn = True
    else:
        loggedIn = False

    template = loader.get_template('WhaleProfiles/index.html')
    context = {
            'user': request.user
    }
    return HttpResponse(template.render(context, request))

def addSpecie(request):
    template = loader.get_template('WhaleProfiles/addSpecie.html')
    return HttpResponse("Where the user can create new species to add data")

def editSpecie(request):
    template = loader.get_template('WhaleProfiles/editSpecie.html')
    return HttpResponse("Where the user can edit already existing species")
