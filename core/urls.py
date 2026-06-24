from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("mes-creations/", views.creations, name="creations"),
    path("projets-jouables/", views.projets_jouables, name="projets_jouables"),
]
