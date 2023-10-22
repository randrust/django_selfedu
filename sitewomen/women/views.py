from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.

menu = [
    {'title': 'About Site', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_article'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'log_in'},
    ]

data_db = [
    {'id': 1, 'title': 'A. Djolly', 'content': '''<h1>Анджелина Джоли</h1> (English Angelina Jolie [7], born Voight, formerly Jolie Pitt; born June 4, 1975, Los Angeles, California, USA) - American film, television and voice actress , film director, screenwriter, producer, fashion model, UN Goodwill Ambassador.
    Winner of an Oscar, three Golden Globe Awards (the first actress in history to win the award three years in a row) and two Screen Actors Guild Awards.''', 'is_published': True},
    {'id': 2, 'title': 'M. Robby', 'content': 'About M. Robby', 'is_published': False},
    {'id': 3, 'title': 'J. Roberts', 'content': 'About J. Roberts', 'is_published': True}  # noqa: E501
    ]

cats_db = [
    {'id': 1, 'name' : "Actresses"},
    {'id': 2, 'name' : "Singers"},
    {'id': 3, 'name' : "Sportswomen"},


]
def index(request):
    data = {
        'title': 'MAIN PAGE',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
        }
    return render(request, "women/index.html", context=data)

def about(request):
    return render(request, "women/about.html", {'title': 'About Site', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'View post with id: {post_id}')

def addarticle(request):
    return HttpResponse('Add artcile')

def contact(request):
    return HttpResponse('Contact')

def login(request):
    return HttpResponse('Log in')

def show_category(request, cat_id):
    data = {
        'title': 'LIST BY CATEGORIES',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
        }
    return render(request, "women/index.html", context=data)


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
