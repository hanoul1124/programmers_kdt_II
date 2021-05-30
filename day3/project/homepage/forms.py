from django import forms
from .models import *


class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'is_ice')
