from django.shortcuts import render
from .models import Person


def home(request):
    persons = Person.objects.all()
    context = {
        'title': 'people',
        'persons': persons
    }
    return render(request, "dq/person_list.html", context)


