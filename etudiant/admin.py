from django.contrib import admin
from .models import USER_ETUDIANT

@admin.register(USER_ETUDIANT)
class USER_Etu_Admin(admin.ModelAdmin):
    list_display=("id","name","email","password") #L'ordre d'affichage des champs 
    fields=["id","name","email","password"] # --> Les champs à afficher ...