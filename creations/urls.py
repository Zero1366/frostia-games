from django.urls import path

from . import views

app_name = "creations"

urlpatterns = [
    path("categories/", views.category_list, name="category_list"),
    path("categories/ajouter/", views.category_create, name="category_create"),
    path("categories/<int:pk>/modifier/", views.category_update, name="category_update"),
    path("categories/<int:pk>/supprimer/", views.category_delete, name="category_delete"),
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/ajouter/", views.tag_create, name="tag_create"),
    path("tags/<int:pk>/modifier/", views.tag_update, name="tag_update"),
    path("tags/<int:pk>/supprimer/", views.tag_delete, name="tag_delete"),
]
