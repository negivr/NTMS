# Generated by Django 3.0 on 2019-12-15 04:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('ssn', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999999999)])),
            ],
        ),
    ]
