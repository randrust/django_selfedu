from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse("Main page women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>List Categories</h1><p>id: {cat_id}")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>List Categories</h1><p>slug: {cat_slug}")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', arg=('music',))
        return redirect(uri)
    return HttpResponse(f"<h1>List By Year</h1><p>slug: {year}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found Completely</h1>")
