# Generated by Django 3.0 on 2019-12-15 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dq', '0002_cdl_employer_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdl',
            name='date_expire',
            field=models.DateField(blank=True, null=True),
        ),
    ]
