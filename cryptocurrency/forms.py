from django import forms
from .models import CryptoCurrency

class AddCryptocurrencyForm(forms.ModelForm):

    class Meta:
        model = CryptoCurrency
        fields = ['name']
