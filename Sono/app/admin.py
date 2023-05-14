from django.contrib import admin
from .models import Album, BandMember, Band, Song, Genre

admin.site.register(Album)
admin.site.register(Band)
admin.site.register(BandMember)
admin.site.register(Song)
admin.site.register(Genre)