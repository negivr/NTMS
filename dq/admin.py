from django.contrib import admin
from .models import Person, Cdl, Employer, Employment


admin.site.register(Person)
admin.site.register(Employer)
admin.site.register(Employment)
admin.site.register(Cdl)

