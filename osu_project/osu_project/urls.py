from django.conf.urls import url
from base import views

urlpatterns = [
        url(r'^$', views.index, name='homepage'),
        url(r'^about/', views.about, name='about'),
        url(r'^events/', views.events, name='events'),
        url(r'^rules/', views.rules, name='rules'),
        url(r'^partners/', views.partners, name='partners'),
        url(r'^contact/', views.contact, name='contact')
]
