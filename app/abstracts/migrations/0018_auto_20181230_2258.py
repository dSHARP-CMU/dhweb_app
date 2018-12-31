# Generated by Django 2.1 on 2018-12-31 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0017_auto_20181230_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='abbreviation',
        ),
        migrations.AddField(
            model_name='conference',
            name='venue_abbreviation',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
