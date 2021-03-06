# Generated by Django 3.0 on 2019-12-15 05:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mc_num', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999999999)])),
                ('dot_num', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999999999)])),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('FMCSA_subject', models.BooleanField(default=False)),
                ('safety_sensitive', models.BooleanField(default=False)),
                ('employer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dq.Employer')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dq.Person')),
            ],
            options={
                'ordering': ['-date_start'],
            },
        ),
        migrations.CreateModel(
            name='Cdl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdl_num', models.CharField(blank=True, max_length=100, null=True)),
                ('cdl_class', models.CharField(blank=True, max_length=100, null=True)),
                ('cdl_state', models.CharField(blank=True, max_length=2, null=True)),
                ('date_issue', models.DateField(null=True)),
                ('date_expire', models.DateField(null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dq.Person')),
            ],
        ),
    ]
