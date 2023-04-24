from django import forms
from .models import Product, OrderInfo

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
        
class CreateOrderInfo(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    adress = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    post_index = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))

    class Meta:
        model = OrderInfo
        fields = ('first_name', 'last_name', 'email', 'adress',
                  'post_index',)
        
class OrderStatus(forms.ModelForm):
    first_name = forms.CharField(required=False, disabled=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg disabled',
    }))
    last_name = forms.CharField(required=False, disabled=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg disabled',
    }))
    email = forms.EmailField(required=False, disabled=True, widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg disabled',
    }))
    adress = forms.CharField(required=False, disabled=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg disabled',
    }))
    post_index = forms.IntegerField(required=False, disabled=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg disabled',
    }))


    status = forms.MultipleChoiceField(required=False, widget=forms.Select(),
                                       choices=(
        ('Передан продавцу', 'Передан продавцу'),
        ('Принят продавцом', 'Принят продавцом'),
        ('В доставке', 'В доставке'),
        ('Получен', 'Получен'),
        ))
    
    class Meta:
        model = OrderInfo
        fields = ('first_name', 'last_name', 'email', 'adress',
                  'post_index','status', )