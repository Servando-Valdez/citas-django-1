from allauth.account.forms import LoginForm
from django import forms

class CustomLoginForm(LoginForm):
    username = None  # Ocultar el campo de nombre de usuario
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def login(self, *args, **kwargs):
        # Asegurarte de que el email se use como nombre de usuario
        self.fields['login'].widget = forms.HiddenInput()  # Ocultar el campo 'login' que generalmente es username o email
        return super(CustomLoginForm, self).login(*args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-control signin-email',
            'placeholder': 'Email address',
            'id': 'signin-email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control signin-password',
            'placeholder': 'Password',
            'id': 'signin-password'
        })