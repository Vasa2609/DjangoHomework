from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('name/', views.name, name='name'),
    path('age/', views.age, name='age'),
    path('hobby/', views.hobby, name='hobby')
]
