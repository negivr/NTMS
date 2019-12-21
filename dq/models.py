from django.db import models
from django.urls import reverse
from .functions import get_uploaded_cdl_file_name

from django.core.validators import MaxValueValidator


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    ssn = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(999999999)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})  # return reverse("people:person-list")


class Cdl(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    cdl_num = models.CharField(max_length=100, null=True, blank=True)
    cdl_class = models.CharField(max_length=100, null=True, blank=True)
    cdl_state = models.CharField(max_length=2, null=True, blank=True) # kasnije dodaj adrese - poseban model
    date_issue = models.DateField(null=True)
    date_expire = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to=get_uploaded_cdl_file_name, null=True, blank=True)

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name} - {self.cdl_num} {self.cdl_state}'


class Employer(models.Model):
    name = models.CharField(max_length=100)
    mc_num = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(999999999)])
    dot_num = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(999999999)])
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.dot_num}'

    def get_absolute_url(self):
        return reverse('employer-detail', kwargs={'pk': self.pk})


class Employment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    employer_name = models.ForeignKey(Employer, on_delete=models.CASCADE)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    salary = models.CharField(max_length=100, null=True, blank=True)
    reason = models.CharField(max_length=100, null=True, blank=True)
    FMCSA_subject = models.BooleanField(default=False)
    safety_sensitive = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_start']

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name} - {self.employer_name} {self.date_start} to {self.date_end}'

    def get_absolute_url(self):
        return reverse('people:employment-list')
