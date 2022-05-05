from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Pizza

def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(
            content={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        }
 )