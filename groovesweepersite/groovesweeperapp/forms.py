from django import forms
from .models import SongQueryModel
import lyricsgenius


class SongQueryForm(forms.ModelForm):
    """
    This code handles details of the search form on the homepage, connects to
    SongQueryModel
    """
    class Meta:
        model = SongQueryModel
        fields = '__all__'
        widgets = {
            'term': forms.TextInput(attrs={'placeholder': 'Search for a song'}),
        }

class FilterForm(forms.Form):
    to_add = forms.CharField(widget=forms.Textarea)
