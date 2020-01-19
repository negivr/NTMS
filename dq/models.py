from django.db import models
from django.urls import reverse, reverse_lazy
from .functions import get_uploaded_cdl_file_name
from .fields import UniqueBooleanFieldTrue, UniqueCharFieldActive

from django.core.validators import MaxValueValidator


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    ssn = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(999999999)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        # return reverse('person-detail', kwargs={'pk': self.pk})  # return reverse("people:person-list")
        return reverse('person-detail', args=[str(self.pk)])

    def get_success_url(self):
        return reverse_lazy('dq:person-detail', kwargs={'pk': self.object.pk})  # proveri da li radi


class Cdl(models.Model):
    STATUSES = (
        ('Active', 'Active'),
        ('Surrendered', 'Surrendered'),
        ('Suspended', 'Suspended'),
        ('Invalid', 'Invalid'),
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    cdl_num = models.CharField(max_length=100, null=True, blank=True)
    cdl_class = models.CharField(max_length=100, null=True, blank=True)
    cdl_state = models.CharField(max_length=2, null=True, blank=True) # kasnije dodaj adrese - poseban model
    isactive = models.BooleanField(default=False)
    # status = models.CharField(max_length=100, null=True, blank=True, choices=STATUSES)
    date_issue = models.DateField(null=True)
    date_expire = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to=get_uploaded_cdl_file_name, null=True, blank=True)

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name} - {self.cdl_num} {self.cdl_state}'

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)


class Medical(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    cdl = models.ForeignKey(Cdl, on_delete=models.CASCADE)
    qualified = models.BooleanField(default=False)
    date_issue = models.DateField(null=True, blank=True)
    date_expire = models.DateField(null=True, blank=True)
    # img = models.ImageField(upload_to=get_uploaded_medical_file_name, null=True, blank=True)

    class Meta:
        ordering = ['date_issue']

    def __str__(self):
        return f'{self.person.first_name} {self.person.last_name} - {self.cdl.cdl_num} {self.date_expire}'


class DrugTest(models.Model):
    TYPE = (
        ('Pre Employment', 'Pre Employment'),
        ('Random', 'Random'),
        ('Post Accident', 'Post Accident'),
        ('Reasonable Suspicion', 'Reasonable Suspicion'),
    )

    RESULTS = (
        ('NEGATIVE', 'NEGATIVE'),
        ('POSITIVE', 'POSITIVE'),
    )

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True, choices=TYPE)
    date_taken = models.DateField(null=True, blank=True)
    date_results = models.DateField(null=True, blank=True)
    results = models.CharField(max_length=100, null=True, blank=True, choices=RESULTS)
    # request_doc = models.FileField(upload_to=get_uploaded_drug_file_name, null=True, blank=True)
    # ccf_doc = models.FileField(upload_to=get_uploaded_drug_file_name, null=True, blank=True)
    # results_doc = models.FileField(upload_to=get_uploaded_drug_file_name, null=True, blank=True)

    class Meta:
        ordering = ['date_results']

    def __str__(self):
        return f'{self.date_results} - {self.person.first_name} {self.person.last_name} - {self.type}: {self.results}'


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


