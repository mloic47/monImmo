from django.http import HttpResponse


def index(request):
    return HttpResponse("Bienvenue sur monImmo. Un reseau social pour immobilier.")
