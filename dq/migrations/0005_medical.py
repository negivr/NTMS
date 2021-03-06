# Generated by Django 3.0 on 2019-12-24 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dq', '0004_cdl_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualified', models.BooleanField(default=False)),
                ('date_issue', models.DateField(blank=True, null=True)),
                ('date_expire', models.DateField(blank=True, null=True)),
                ('cdl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dq.Cdl')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dq.Person')),
            ],
        ),
    ]
