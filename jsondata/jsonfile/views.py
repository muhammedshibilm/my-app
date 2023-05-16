from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Quote

# Create your views here.

def index(request):
    return HttpResponse("Hello")



def json(request):
    data = {
        "message": "Hello, world!",
        "count": 10,
        "is_valid": True
    }
    return JsonResponse(data)

def quote_list(request):
    quotes = Quote.objects.all()
    data = {"quotes": list(quotes.values())}
    return JsonResponse(data)
