from django.contrib import admin
from django.urls import path
from .import views

app_name="etudiant"

urlpatterns = [
    path("gestion_etudiant/" ,views.add_show , name="ajouter_etudiant"),
    path("modifier/<int:book_id>/" , views.modifier , name="edit_student"),
    path("supprimer/<int:book_id>/" , views.supprimer , name="remove_student"),
    path('comfirmation_delete_article/<int:book_id>/',views.comfirm_delete, name='comfirme_delete'),
]
