from django.shortcuts import render
from .models import Person


def home(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, "dq/_table_person.html", context)


