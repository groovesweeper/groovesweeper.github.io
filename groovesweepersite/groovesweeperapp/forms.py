from django import forms
from .models import SongQueryModel
import lyricsgenius


class SongQueryForm(forms.ModelForm):
    class Meta:
        model = SongQueryModel
        fields = '__all__'

class FilterForm(forms.Form):
    to_add = forms.CharField(widget=forms.Textarea)
