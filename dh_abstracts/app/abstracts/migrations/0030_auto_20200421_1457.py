# Generated by Django 3.0.5 on 2020-04-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstracts', '0029_auto_20200420_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.CharField(db_index=True, max_length=500),
        ),
    ]
