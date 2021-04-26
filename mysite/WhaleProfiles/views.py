from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Specie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View

class Index(View):
    allUsers = User.objects.all()
    whales = Specie.objects.all()
    def get(self, request):
        context = {
        'allUsers': self.allUsers,
        'whales': self.whales
        }

        template = loader.get_template('WhaleProfiles/index.html')
        return HttpResponse(template.render(context, request))

    def post(self, request):
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
        'allUsers': self.allUsers,
        'whales': self.whales
        }
        print(context)
        template = loader.get_template('WhaleProfiles/index.html')
        return HttpResponse(template.render(context, request))
class AddSpecie(View):
    whales = Specie.objects.all()
    def get(self, request):
        context = {
        'whales': self.whales
        }
        template = loader.get_template('WhaleProfiles/addSpecie.html')
        return HttpResponse(template.render(context, request))

    def post(self, request):
        if request.method == "POST":
            inputName = request.POST['name']
            inputNumber = request.POST['numWhales']
            inputDiet = request.POST['diet']
            inputSize = request.POST['size']
            inputWeight = request.POST['weight']

        whale = Specie(
            name = inputName,
            numWhales = inputNumber,
            diet = inputDiet,
            size = inputSize,
            weight = inputWeight
        )

        whale.save()

        context = {
        'whales': self.whales
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
