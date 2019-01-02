# Generated by Django 2.1 on 2019-01-02 02:58

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("abstracts", "0027_auto_20190101_2152")]

    operations = [
        migrations.RemoveIndex(model_name="work", name="full_text_idx"),
        migrations.AddField(
            model_name="work",
            name="search_vector",
            field=django.contrib.postgres.search.SearchVectorField(
                editable=False, null=True
            ),
        ),
        migrations.AddIndex(
            model_name="work",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="full_text_idx"
            ),
        ),
    ]
