from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Specie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View

class Index(View):
    def get(self, request):
        allUsers = User.objects.all()
        whales = Specie.objects.all()
        if request.method == "POST":
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

        context = {
        'allUsers': allUsers,
        'whales': whales
        }

        template = loader.get_template('WhaleProfiles/index.html')
        return HttpResponse(template.render(context, request))
class AddSpecie(View):
    def get(self, request):
        context = {

        }
        template = loader.get_template('WhaleProfiles/addSpecie.html')
        return HttpResponse(template.render(context, request))

class EditSpecie(View):
    def get(self, request):
        whales = Specie.objects.all()
        context = {
                'whales': whales
        }
        template = loader.get_template('WhaleProfiles/editSpecie.html')
        return HttpResponse(template.render(context, request))
