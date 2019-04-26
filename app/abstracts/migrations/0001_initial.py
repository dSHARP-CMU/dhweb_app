# Generated by Django 2.1 on 2019-04-26 01:02

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, default='', max_length=500)),
            ],
            options={
                'ordering': ['institution', 'department'],
            },
        ),
        migrations.CreateModel(
            name='Appellation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, db_index=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, db_index=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorship_order', models.PositiveSmallIntegerField(default=1)),
                ('affiliations', models.ManyToManyField(blank=True, related_name='asserted_by', to='abstracts.Affiliation')),
                ('appellation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asserted_by', to='abstracts.Appellation')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorships', to='abstracts.Author')),
            ],
            options={
                'ordering': ['authorship_order'],
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('venue', models.CharField(max_length=100)),
                ('venue_abbreviation', models.CharField(blank=True, max_length=25)),
                ('notes', models.TextField(blank=True, default='')),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='ConferenceSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('abbreviation', models.CharField(blank=True, max_length=7, unique=True)),
                ('notes', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgn_id', models.URLField(max_length=100, unique=True)),
                ('pref_name', models.CharField(db_index=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CountryLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=300)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='abstracts.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FileImportMessgaes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('addition_type', models.CharField(choices=[('mat', 'matched existing'), ('new', 'newly created'), ('non', 'NA')], default='non', max_length=3)),
                ('warning', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FileImportTries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started', models.DateTimeField(auto_now_add=True)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstracts.Conference')),
                ('file_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstracts.FileImport')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institutions', to='abstracts.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('author_supplied', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('full_text', models.TextField(max_length=100000)),
                ('display_abbreviation', models.CharField(max_length=50, unique=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('abbreviation', models.CharField(blank=True, max_length=7, unique=True)),
                ('notes', models.TextField(blank=True)),
                ('url', models.URLField(blank=True, max_length=100)),
                ('conferences_organized', models.ManyToManyField(blank=True, related_name='organizers', to='abstracts.Conference')),
            ],
        ),
        migrations.CreateModel(
            name='SeriesMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(blank=True)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_memberships', to='abstracts.Conference')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conference_memberships', to='abstracts.ConferenceSeries')),
            ],
            options={
                'ordering': ['-conference__year'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', django.contrib.postgres.search.SearchVectorField(editable=False, null=True)),
                ('title', models.CharField(max_length=500)),
                ('state', models.CharField(choices=[('ac', 'accpeted'), ('su', 'submission')], max_length=2)),
                ('full_text', models.TextField(blank=True, default='', max_length=50000)),
                ('full_text_type', models.CharField(choices=[('xml', 'XML'), ('txt', 'plain text')], default='txt', max_length=3)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='abstracts.Conference')),
                ('disciplines', models.ManyToManyField(blank=True, related_name='works', to='abstracts.Discipline')),
                ('full_text_license', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='abstracts.License')),
                ('keywords', models.ManyToManyField(blank=True, related_name='works', to='abstracts.Keyword')),
                ('languages', models.ManyToManyField(blank=True, related_name='works', to='abstracts.Language')),
                ('published_version', models.ForeignKey(blank=True, limit_choices_to={'state': 'ac'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unpublished_versions', to='abstracts.Work')),
                ('topics', models.ManyToManyField(blank=True, related_name='works', to='abstracts.Topic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='work',
            name='work_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='abstracts.WorkType'),
        ),
        migrations.AddField(
            model_name='fileimportmessgaes',
            name='attempt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstracts.FileImportTries'),
        ),
        migrations.AddField(
            model_name='conference',
            name='series',
            field=models.ManyToManyField(related_name='conferences', through='abstracts.SeriesMembership', to='abstracts.ConferenceSeries'),
        ),
        migrations.AddField(
            model_name='authorship',
            name='genders',
            field=models.ManyToManyField(blank=True, related_name='asserted_by', to='abstracts.Gender'),
        ),
        migrations.AddField(
            model_name='authorship',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authorships', to='abstracts.Work'),
        ),
        migrations.AddField(
            model_name='author',
            name='appellations',
            field=models.ManyToManyField(related_name='authors', through='abstracts.Authorship', to='abstracts.Appellation'),
        ),
        migrations.AddField(
            model_name='author',
            name='works',
            field=models.ManyToManyField(related_name='authors', through='abstracts.Authorship', to='abstracts.Work'),
        ),
        migrations.AlterUniqueTogether(
            name='appellation',
            unique_together={('first_name', 'last_name')},
        ),
        migrations.AddField(
            model_name='affiliation',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='affiliations', to='abstracts.Institution'),
        ),
        migrations.AddIndex(
            model_name='work',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_text'], name='abstracts_w_search__cfd9ce_gin'),
        ),
        migrations.AlterUniqueTogether(
            name='seriesmembership',
            unique_together={('series', 'number')},
        ),
        migrations.AlterUniqueTogether(
            name='institution',
            unique_together={('name', 'country')},
        ),
        migrations.AlterUniqueTogether(
            name='authorship',
            unique_together={('author', 'work'), ('work', 'authorship_order')},
        ),
        migrations.AlterUniqueTogether(
            name='affiliation',
            unique_together={('department', 'institution')},
        ),
    ]
