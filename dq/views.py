from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from .models import Person, Cdl
from .forms import PersonModelForm, CdlModelForm
from django.forms import inlineformset_factory

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
    if cdls:
        active_cdl = get_object_or_404(cdls, isactive=True)  # active_cdl = get_object_or_404(cdls, date_expire__isnull=True)
        context = {
            'person': person,
            'active_cdl': active_cdl,
            'cdls': cdls
        }
    else:
        context = {
            'person': person,
            'active_cdl': '',
            'cdls': ''
        }
    template_name = 'dq/person_detail.html'

    return render(request, template_name, context)


def person_create(request):
    template_name = 'dq/person_form.html'
    form = PersonModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dq:person-list')
        # return redirect(reverse_lazy('dq:person-detail', kwargs={'pk': id}))  # ne radi
    return render(request, template_name, {'form': form})


def cdl_list(request):
    cdls = Cdl.objects.all()
    context = {
        'title': 'cdls',
        'cdls': cdls
    }
    return render(request, "dq/cdl_list.html", context)


def cdl_create(request):
    template_name = 'dq/cdl_form.html'
    form = CdlModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dq:cdl-list')
    return render(request, template_name, {'form': form})


def person_cdl_create(request, pk):
    person = Person.objects.get(id=pk)
    CdlFormSet = inlineformset_factory(Person, Cdl, fields='__all__')
    formset = CdlFormSet(instance=person)  # form = CdlModelForm(request.POST or None)
    if request.method == 'POST':
        formset = CdlFormSet(request.POST, instance=person)
        if formset.is_valid():
            formset.save()
            return redirect('dq:cdl-list')
    context = {
        'formset': formset
    }
    return render(request, 'dq/cdl_form.html', context)





