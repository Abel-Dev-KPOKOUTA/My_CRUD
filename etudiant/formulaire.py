from django import forms 
from django.core import validators
from .models import USER_ETUDIANT

class UserForms(forms.ModelForm):
    class Meta:
        model=USER_ETUDIANT
        fields=["name","email","password"]
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True , attrs={'class':'form-control'}),
        }
        
    def clean_password(self):
        password=self.cleaned_data["password"]
        if len(password)<6 :
            raise forms.ValidationError("Minimum 6 caractères pour le mot de passe ....!")
        
        return password