from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from userauth.models import User, Seller
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    phone = forms.CharField(widget=RegionalPhoneNumberWidget(region='RU', attrs={
        'class': 'form-control form-control-lg',
    }))
    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control form-control-lg',
        'type': 'date',
    }))
    # gender = forms.ChoiceField(widget=forms.CheckboxInput(attrs={
    #     'class': 'form-control form-control-lg',
    # }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone', "birth_date")



class SellerLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    class Meta:
        model = Seller
        fields = ('username', 'password')

class SellerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    shop_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    org_type = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    inn_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    store_tags = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
    }))

    class Meta:
        model = Seller
        fields = ('username', 'shop_name', 'org_type', 'inn_code', 'store_tags', 'email', 'password1', 'password2')