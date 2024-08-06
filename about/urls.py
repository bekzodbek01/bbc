from django.contrib import admin
from about.views import *
from django.urls import path

urlpatterns = [
    path('about/', AboutListView.as_view(), name='about-list'),
    path('about/<int:pk>/', Aboutdetail, name='about-detail'),

    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', Newsdetail, name='news-detail'),

    path('connection/', ConnectionListView.as_view(), name='connection-list'),
    path('connection/<int:pk>/', Connectiondetail, name='connection-detail'),

    path('contact/', ContactListView.as_view(), name='contact-list'),
    path('contact/<int:pk>/', Contactdetail, name='contact-detail'),
]