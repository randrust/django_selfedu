from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.

menu = [
    {'title': 'About Site', 'url_name': 'about'},
    {'title': 'Add aticle', 'url_name': 'add_aticle'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'log_in'},
    ]

data_db = [
    {'id': 1, 'title': 'A. Djolly', 'content': 'About A. Djolly', 'is_published': True},
    {'id': 2, 'title': 'M. Robby', 'content': 'About M. Robby', 'is_published': False},
    {'id': 3, 'title': 'J. Roberts', 'content': 'About J. Roberts', 'is_published': True}  # noqa: E501
    ]
def index(request):
    data = {
        'title': 'MAIN PAGE',
        'menu': menu,
        'posts': data_db
        }
    return render(request, "women/index.html", context=data)

def about(request):
    return render(request, "women/about.html", {'title': 'About Site'})


def show_post(request, post_id):
    return HttpResponse(f'View post with id: {post_id}')

def addaticle(request):
    return HttpResponse('Add atcile')

def contact(request):
    return HttpResponse('Contact')

def login(request):
    return HttpResponse('Log in')


# def categories(request, cat_id):
#     return HttpResponse(f"<h1>List Categories</h1><p>id: {cat_id}")


# def categories_by_slug(request, cat_slug):
#     return HttpResponse(f"<h1>List Categories</h1><p>slug: {cat_slug}")


# def archive(request, year):
#     if year > 2023:
#         uri = reverse('cats', args=('sport',))
#         return redirect(uri)
#     return HttpResponse(f"<h1>List By Year</h1><p>slug: {year}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found Completely</h1>")
