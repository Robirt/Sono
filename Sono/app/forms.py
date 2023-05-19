from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Band, BandMember, Genre, Product, Rental
from .models import Song
from .models import Album

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

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