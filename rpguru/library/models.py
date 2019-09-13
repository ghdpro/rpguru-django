"""RPGuru Library Models"""

from pathlib import Path

from django.db import models
from django.utils.text import slugify

from ..core.models import Language


def artwork_upload_location(instance, filename):
    # Pattern: [artwork_root]/[instance id].jpg
    return Path(slugify(instance.__class__.__name__), '{0}.jpg'.format(instance.id))


class Platform(models.Model):
    name = models.CharField('name', max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    short = models.CharField('short name', max_length=100)
    artwork = models.ImageField(upload_to=artwork_upload_location, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Franchise(models.Model):
    name = models.CharField('name', max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    artwork = models.ImageField(upload_to=artwork_upload_location, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField('name', max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    artwork = models.ImageField(upload_to=artwork_upload_location, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Companies'


class Genre(models.Model):
    name = models.CharField('name', max_length=250)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    class Verdict:
        GOOD = 1
        OKAY = 2
        BAD = 3
        choices = (
            (GOOD, 'Good'),
            (OKAY, 'Okay'),
            (BAD, 'Bad')
        )
    title = models.CharField('title', max_length=250)
    artwork = models.ImageField(upload_to=artwork_upload_location, blank=True)
    jp_date = models.DateField('Japanese Release Date', null=True, blank=True)
    na_date = models.DateField('North America Release Date', null=True, blank=True)
    eu_date = models.DateField('Europe Release Date', null=True, blank=True)
    audio = models.ManyToManyField(Language)
    franchise_main = models.ForeignKey(Franchise, related_name='main',
                                       null=True, blank=True, on_delete=models.SET_NULL)
    franchise_side = models.ForeignKey(Franchise, related_name='side',
                                       null=True, blank=True, on_delete=models.SET_NULL)
    platform = models.ManyToManyField(Platform)
    developer = models.ManyToManyField(Company, related_name='developer')
    publisher = models.ManyToManyField(Company, related_name='publisher')
    genre = models.ManyToManyField(Genre)
    verdict = models.PositiveSmallIntegerField('verdict', choices=Verdict.choices, default=Verdict.GOOD)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
