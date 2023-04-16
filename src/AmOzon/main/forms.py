from django import forms
from .models import Product

class CreateProduct(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control form-control-lg',
    }))
    parameters = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control form-control-lg',
    }))
    price = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    category = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control form-control-lg',
    }))
    image = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control form-control-lg',
    }))

    class Meta:
        model = Product
        fields = ('title', 'description', 'parameters', 'price',
                  'category', 'image',)