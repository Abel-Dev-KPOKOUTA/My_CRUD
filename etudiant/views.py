from django.shortcuts import render , redirect
from django.http import HttpResponse
from .formulaire import UserForms
from .models import USER_ETUDIANT

def add_show(request):
    if request.method=="POST":
        formular=UserForms(request.POST)
        if formular.is_valid():
            formular.save()
            return redirect("etudiant:ajouter_etudiant")
    else:
        formular=UserForms()
    
    students=USER_ETUDIANT.objects.all()
    context={"formular":formular,"students":students}
    return render(request ,"etudiant/add_and_show.html",context)

def modifier(request , book_id):
    etudiant=USER_ETUDIANT.objects.get(pk=book_id)
    if request.method=='POST':
        formular=UserForms(request.POST,instance=etudiant)
        if formular.is_valid():
            formular.save()
            return redirect("etudiant:ajouter_etudiant")
    else:
        formular=UserForms(instance=etudiant)
    
    context={"formular":formular}
    return render(request, "etudiant/updates_student.html",context)


def supprimer(request,book_id):
    etudiant=USER_ETUDIANT.objects.get(pk=book_id)
    etudiant.delete()
    return redirect("etudiant:ajouter_etudiant")

def comfirm_delete(request, book_id):
    etudiant=USER_ETUDIANT.objects.get(pk=book_id)
    return render(request,'etudiant/comfirmation_delete.html',{"etudiant":etudiant})
    
