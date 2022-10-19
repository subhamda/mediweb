from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("client",views.client,name="client"),
    path("contact",views.contact,name="contact"),
    path("product",views.product,name="product"),
]