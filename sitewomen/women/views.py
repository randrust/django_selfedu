from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.

menu = ['About Site', 'Add aticle', 'Contact', 'Log in']

class MyClass():
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    data = {
        'title': 'MAIN PAGE',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1,2,3,2,5},
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'obj': MyClass(5, 10)
        }
    return render(request, "women/index.html", context=data)

def about(request):
    return render(request, "women/about.html", {'title': 'About Site'})


def categories(request, cat_id):
    return HttpResponse(f"<h1>List Categories</h1><p>id: {cat_id}")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>List Categories</h1><p>slug: {cat_slug}")


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('sport',))
        return redirect(uri)
    return HttpResponse(f"<h1>List By Year</h1><p>slug: {year}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found Completely</h1>")
