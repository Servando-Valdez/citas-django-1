from allauth.account.forms import LoginForm, SignupForm
from django import forms

class CustomLoginForm(LoginForm):
    username = None  # Ocultar el campo de nombre de usuario
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def login(self, *args, **kwargs):
        # Asegurarte de que el email se use como nombre de usuario
        self.fields['login'].widget = forms.HiddenInput()  # Ocultar el campo 'login' que generalmente es username o email
        return super(CustomLoginForm, self).login(*args, **kwargs)

from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control signup-username',
            'placeholder': 'Username',
            'id': 'signup-username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control signup-email',
            'placeholder': 'Email',
            'id': 'signup-email'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control signup-password',
            'placeholder': 'Create a password',
            'id': 'signup-password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control signup-password',
            'placeholder': 'Confirm your password',
            'id': 'signup-password2'
        })
    )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Aquí puedes agregar lógica adicional si es necesario
        return user
