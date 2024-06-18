from django.urls import path
from . import views

urlpatterns = [
    path("" , views.homepage , name="home"),
    path("franchise-details/" , views.franchise_page , name="franchise")
]