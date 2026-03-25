from django import forms
from .models import Prihlaska, Kruzok

class PrihlaskaForm(forms.ModelForm):
    class Meta:
        model = Prihlaska
        fields = ['meno', 'email', 'kruzok', 'sprava']


class KruzokForm(forms.ModelForm):
    class Meta:
        model = Kruzok
        fields = ['nazov', 'den', 'veduci']