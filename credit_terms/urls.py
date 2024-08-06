from django.contrib import admin
from django.urls import path
from credit_terms.views import credit_termsdetail,credit_termsListView

urlpatterns = [
    path('credit/', credit_termsListView.as_view(), name='credit-list'),
    path('credit/<int:pk>/', credit_termsdetail, name='credit-detail'),
]