from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Person, Cdl


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'dob', 'ssn')  # mislio sam da treba list []
        labels = {
            'first_name': _('First name'),
            'last_name': _('First name'),
            'dob': _('DOB'),
            'ssn': _('SSN'),
        }


class CdlModelForm(forms.ModelForm):
    class Meta:
        model = Cdl
        fields = ('cdl_num', 'cdl_class', 'cdl_state', 'isactive', 'date_issue', 'date_expire', 'img')  # '__all__'
        labels = {
            'cdl_num': _('CDL#'),
            'cdl_class': _('Class'),
            'cdl_state': _('State'),
            'isactive': _('Status'),
            'date_issue': _('Issue date'),
            'date_expire': _('Expiration date'),
            'img': _('Image'),
        }


