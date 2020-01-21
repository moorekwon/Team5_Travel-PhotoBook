from django import forms

from photobook.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo_page', 'photo')