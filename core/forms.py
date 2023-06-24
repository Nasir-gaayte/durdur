from django import forms
from .models import CardMolel


class CardForm(forms.ModelForm):
    class Meta:
        model = CardMolel
        fields = '__all__'