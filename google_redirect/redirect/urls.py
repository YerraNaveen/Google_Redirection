from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('g',views.google,name='google_redirect'),
]
