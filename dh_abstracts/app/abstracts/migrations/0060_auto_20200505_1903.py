# Generated by Django 3.0.5 on 2020-05-05 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0059_auto_20200505_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conferenceseries',
            options={'ordering': ['abbreviation']},
        ),
    ]
