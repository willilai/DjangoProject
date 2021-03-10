from django.http import HttpResponse


def index(request):
    return HttpResponse("Account Login/Sign Up, Species list to see data for each species. ")
