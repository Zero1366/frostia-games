from django.urls import path
 
from . import views
 
app_name = "creations"
 
urlpatterns = [
    path("categories/", views.category_list, name="category_list"),
    path("categories/ajouter/", views.category_create, name="category_create"),
    path("categories/<int:pk>/modifier/", views.category_update, name="category_update"),
    path("categories/<int:pk>/supprimer/", views.category_delete, name="category_delete"),
]