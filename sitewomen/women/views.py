from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Main page women")

def categories(request):
    return HttpResponse("<h1>List Categories</h1>")