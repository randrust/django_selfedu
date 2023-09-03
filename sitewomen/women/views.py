from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Main page women")

def categories(request, cat_id):
    return HttpResponse(f"<h1>List Categories</h1><p>id: {cat_id}")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>List Categories</h1><p>slug: {cat_slug}")

def archive(request, year):
    return HttpResponse(f"<h1>List By Year</h1><p>slug: {year}")