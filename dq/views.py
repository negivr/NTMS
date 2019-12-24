from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Person, Cdl

'''
messages.success(request, f'Ovde ubaci poruku koju zelis {person.first_name}')
https://docs.djangoproject.com/en/3.0/ref/contrib/messages/
'''


def home(request):
    persons = Person.objects.all()
    context = {
        'title': 'people',
        'persons': persons
    }
    return render(request, "dq/person_list.html", context)


def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    cdls = Cdl.objects.filter(person=person)
    active_cdl = get_object_or_404(cdls, status="Active")  # active_cdl = get_object_or_404(cdls, date_expire__isnull=True)
    template_name = 'dq/person_detail.html'
    context = {
        'person': person,
        'active_cdl': active_cdl,
        'cdls': cdls
    }
    return render(request, template_name, context)


def cdl_list(request):
    cdls = Cdl.objects.all()
    context = {
        'title': 'cdls',
        'cdls': cdls
    }
    return render(request, "dq/cdl_list.html", context)
