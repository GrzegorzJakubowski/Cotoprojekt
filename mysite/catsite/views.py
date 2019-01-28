from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import koty

# Create your views here.

def wyswietl(request):
    wszystko = koty.objects.all()
    return render_to_response('nazwa', {'wszystko' : wszystko})
