from django import forms
import lyricsgenius


class SongQueryForm(forms.Form):
    term = forms.CharField(label='Your name', max_length=100)
