from django.db import models
from django_countries.fields import CountryField


class Products(models.Model):
    MOVIE_GENRE_CHOICES = [
        ('actn', 'Action & Adventure'),
        ('advn', 'Adventure'),
        ('anim', 'Animation'),
        ('comdy', 'Comedy'),
        ('drm', 'Drama'),
        ('fntsy', 'Fantasy'),
        ('hist', 'History'),
        ('hrrr', 'Horror'),
        ('noir', 'noir'),
        ('scnc', 'Science - Fiction'),
        ('thril', 'Mystery & Thriller'),
        ('west', 'Western'),
        ('ir', 'Iran'),
        ('crim', 'Crime'),
        ('docu', 'Documentary'),
        ('kds', 'Kids & Family'),
        ('music', 'Music & Musical'),
        ('romn', 'Romance'),
        ('sport', 'Sport'),
        ('war', 'War & Military'),
        ('real','Reality'),

    ]

    MOVIE_QUALITY_CHOICES = [
        ('240', '240'),
        ('720', '720'),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
        ('', ''),
    ]
    MOVIE_AGE_RATE_CHOICES = [
        ('all', 'all'),
        ('6', '<6'),
        ('9', '6-9'),
        ('12', '9-12'),
        ('16', '12-16'),
    ]
    MOVIE_LANGUAGE_CHOICES = [
        ('fa', 'persian'),
        ('en', 'english'),
        ('', ''),
        ('', ''),
        ('', ''),
    ]
    MOVIE_CONTINENT_CHOICES = [
        ('asia', 'Asia'),
        ('afrc', 'Africa'),
        ('eu', 'Europe'),
        ('Namrc', 'North America'),
        ('Samrc', 'South America'),
        ('aus', 'Australia/Oceania'),
    ]
    genre = models.CharField(max_length=5, choices=MOVIE_GENRE_CHOICES)
    rating = models.DecimalField(max_length=1, max_digits=3)
    oscar_win = models.BooleanField()
    golden_glob_win = models.BooleanField()
    country = CountryField()
    quality = models.CharField(max_length=5, choices=MOVIE_QUALITY_CHOICES)
    title = models.CharField(max_length=40)
    release_year = models.DateTimeField()
    runtime = models.TimeField()
    description = models.TextField(max_length=200)
    age_rate = models.CharField(max_length=5, choices=MOVIE_AGE_RATE_CHOICES)
    language = models.CharField(max_length=5, choices=MOVIE_LANGUAGE_CHOICES)
    continent = models.CharField(max_length=5, choices=MOVIE_CONTINENT_CHOICES)


class Person(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='countries')
