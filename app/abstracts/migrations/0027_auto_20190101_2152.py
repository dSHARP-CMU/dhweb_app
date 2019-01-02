# Generated by Django 2.1 on 2019-01-02 02:52

import django.contrib.postgres.indexes
from django.contrib.postgres.operations import BtreeGinExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("abstracts", "0026_auto_20190101_1446")]

    operations = [
        BtreeGinExtension(),
        migrations.AlterModelOptions(name="author", options={}),
        migrations.AddIndex(
            model_name="work",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["full_text"], name="full_text_idx"
            ),
        ),
    ]
