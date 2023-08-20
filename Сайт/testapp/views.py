from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('Главная страница<hr>'
                        '<a href="/contacts">Контакты</a><br>'
                        '<a href="/about-us">О нас</a>')
def about_us(request):
    return HttpResponse('Жавохир Неъматов<hr>'
                        '<a href="/">Главная страница</a>')
def contacts(request):
    return HttpResponse('+998997269811<hr>'
                        '<a href="/">Главная страница</a>')
