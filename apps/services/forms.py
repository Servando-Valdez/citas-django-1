from django import forms
from django.forms import ModelForm
from .models import Services

class ServiceForm(ModelForm):
    class Meta:
        model = Services
        fields = ['name',  'price', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        exists_name = Services.objects.filter(name__iexact=name).exclude(id=self.instance.id).exists()
        if exists_name:
            raise forms.ValidationError('This service name already exists')
        return name

