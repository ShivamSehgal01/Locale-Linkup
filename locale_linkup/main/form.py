from django import forms
from django.contrib.auth.models import User
from .models import *

class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    price = forms.DecimalField(label='Price', min_value=0, max_digits=10, decimal_places=2)
    seller = forms.CharField(label='Seller', max_length=100)

    class Meta:
        model = Product
        fields = ['name', 'price', 'seller', 'image']
    