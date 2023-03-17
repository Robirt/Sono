from django.db import models
from django.contrib.auth.models import User

class Band(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='band_images/', null=True, blank=True)

class BandMember(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    role = models.CharField(max_length=32)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

class Genre(models.Model):
    name = models.CharField(max_length=32)

class Album(models.Model):
    title = models.CharField(max_length=32)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='album_covers/', null=True, blank=True)

class Song(models.Model):
    title = models.CharField(max_length=32)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class Rental(models.Model):
    reservation_date = models.DateField()
    reservation_expire_date = models.DateField()
    return_date = models.DateField()
    renter = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Product(models.Model):
    album = models.ForeignKey(Album, on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=64)
    rental = models.ForeignKey(Rental, null=True, on_delete=models.DO_NOTHING)
