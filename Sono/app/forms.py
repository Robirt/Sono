from django import forms
from .models import Band, BandMember, Genre, Product, Rental
from .models import Song
from .models import Album

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'band', 'cover']

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'image']

class BandMemberForm(forms.ModelForm):
    class Meta:
        model = BandMember
        fields = ['first_name', 'last_name', 'role', 'band']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['reservation_date', 'reservation_expire_date', 'return_date', 'renter']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['album', 'code', 'rental']