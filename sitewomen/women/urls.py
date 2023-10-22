from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('addarticle/', views.addarticle, name='add_article'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='log_in'),
    path('category/<int:cat_id>', views.show_category, name='category'),
    # path('cats/<int:cat_id>/', views.categories, name='cat_id'),
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # path('archive/<year4:year>/', views.archive, name='archive'),
]


