from django.conf.urls import url
from base import views

urlpatterns = [
        url(r'^$', views.index, name='homepage'),
        url(r'^location/', views.location, name='location'),
        url(r'^menus/', views.menus, name='menus'),
        url(r'^schedule/', views.schedule, name='schedule'),
        url(r'^rules/', views.rules, name='rules'),
        url(r'^registration/', views.registration, name='registration'),
        url(r'^contact/', views.contact, name='contact')
]
