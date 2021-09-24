from django.contrib import admin
from django.urls import path
from hrushi import views

urlpatterns = [
    path("", views.index, name="home"),
    path("games", views.games, name="games"),
    path("artworks", views.artworks, name="artworks"),
    path("others", views.others, name="others"),
    path("old", views.mainOld, name="old")
]