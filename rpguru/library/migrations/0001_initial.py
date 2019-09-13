# Generated by Django 2.2.5 on 2019-09-13 09:37

from django.db import migrations, models
import django.db.models.deletion
import rpguru.library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('artwork', models.ImageField(blank=True, upload_to=rpguru.library.models.artwork_upload_location)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('artwork', models.ImageField(blank=True, upload_to=rpguru.library.models.artwork_upload_location)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('short', models.CharField(max_length=100, verbose_name='short name')),
                ('artwork', models.ImageField(blank=True, upload_to=rpguru.library.models.artwork_upload_location)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('artwork', models.ImageField(blank=True, upload_to=rpguru.library.models.artwork_upload_location)),
                ('jp_date', models.DateField(blank=True, null=True, verbose_name='Japanese Release Date')),
                ('na_date', models.DateField(blank=True, null=True, verbose_name='North America Release Date')),
                ('eu_date', models.DateField(blank=True, null=True, verbose_name='Europe Release Date')),
                ('verdict', models.PositiveSmallIntegerField(choices=[(1, 'Good'), (2, 'Okay'), (3, 'Bad')], default=1, verbose_name='verdict')),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('audio', models.ManyToManyField(to='core.Language')),
                ('developer', models.ManyToManyField(related_name='developer', to='library.Company')),
                ('franchise_main', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main', to='library.Franchise')),
                ('franchise_side', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='side', to='library.Franchise')),
                ('genre', models.ManyToManyField(to='library.Genre')),
                ('platform', models.ManyToManyField(to='library.Platform')),
                ('publisher', models.ManyToManyField(related_name='publisher', to='library.Company')),
            ],
        ),
    ]
