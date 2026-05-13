

from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserDetails
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput()
        }

from django import forms
from .models import UserDetails

class LoginForm(forms.ModelForm):

    class Meta:
        model = UserDetails
        fields = ['email', 'password']

        widgets = {

            'email': forms.EmailInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Enter email'
            }),

            'password': forms.PasswordInput(attrs={
                'autocomplete': 'off',
                'placeholder': 'Enter password'
            })

        }