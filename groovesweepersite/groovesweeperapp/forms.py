from django.forms import ModelForm
from .models import SongQueryModel
import lyricsgenius


class SongQueryForm(ModelForm):
    class Meta:
        model = SongQueryModel
        fields = '__all__'
