from django.urls import path
from . import views


urlpatterns=[
    path('newstore/', views.newstore, name="store"),


]