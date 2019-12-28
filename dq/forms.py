from django import forms
from .models import Person, Cdl


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'dob', 'ssn')  # mislio sam da treba list []


class CdlModelForm(forms.ModelForm):
    class Meta:
        model = Cdl
        fields = '__all__'



