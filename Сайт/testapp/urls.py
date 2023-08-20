from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about-us', views.about_us),
    path('contacts', views.contacts),
]