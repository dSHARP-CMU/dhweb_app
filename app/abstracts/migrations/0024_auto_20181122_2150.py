# Generated by Django 2.1 on 2018-11-23 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0023_auto_20181122_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seriesmembership',
            name='number',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
