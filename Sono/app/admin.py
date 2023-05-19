from django.contrib import admin
from .models import Rental, Product, Album, Band, Song, BandMember, Genre

admin.site.register(Rental)
admin.site.register(Product)
admin.site.register(Album)
admin.site.register(Band)
admin.site.register(Song)
admin.site.register(BandMember)
admin.site.register(Genre)
