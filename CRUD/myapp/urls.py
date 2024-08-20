from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('database', views.show, name='show'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.deletee, name='deletee')

]
