# Generated by Django 3.0.5 on 2020-07-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0065_remove_keyword_author_supplied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='end_date',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AlterField(
            model_name='conference',
            name='start_date',
            field=models.DateField(blank=True, help_text='YYYY-MM-DD', null=True),
        ),
    ]
