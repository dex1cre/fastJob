from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    perks = Perk.objects.all()
    return render(request, "findJob/index.html", {'perks':perks})
