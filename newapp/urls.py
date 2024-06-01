"""
Defines the URL patterns for the newapp application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
