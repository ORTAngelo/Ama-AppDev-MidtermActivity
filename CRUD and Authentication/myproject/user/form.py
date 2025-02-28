from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Product

class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", max_length=20 ,widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Username'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        

        self.fields['password1'].widget.attrs['class'] = 'input-box'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"></ul>'

        self.fields['password2'].widget.attrs['class'] = 'input-box'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"></span>'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['serial_number', 'product_name', 'price']
