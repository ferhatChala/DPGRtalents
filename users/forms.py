from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Doctorant

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctorant
        fields = ['phone','Adress','master_D']