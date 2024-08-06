from django.contrib import admin
from django.urls import path
from car.views import *
urlpatterns = [
    path('logo/', LogoListView.as_view(), name='Logo-list'),
    path('logo/<int:pk>/', Logodetail, name='Logo-detail'),

    path('car/', CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/', Cardetail, name='car-detail'),

    path('contract/', ContractListView.as_view(), name='contract-list'),
    path('contract/<int:pk>/', Contractdetail, name='contract-detail'),

    path('silder/', SilderListView.as_view(), name='silder-list'),
    path('silder/<int:pk>/', Silderdetail, name='silder-detail'),

]