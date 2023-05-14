from django import forms
from .models import Genre
from .models import Song

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title']