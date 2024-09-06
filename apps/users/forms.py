from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User

class CustomSignupForm(SignupForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
        required=True,
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
