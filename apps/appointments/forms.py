from datetime import datetime
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #date value is set to today by default
        self.fields['date'].initial = datetime.now().date()
    class Meta:
        model = Appointment
        fields = ['service', 'price', 'date', 'time']
        # fields = ['service', 'price', 'date']
        widgets = {
            'time': forms.Select(attrs={
                #'type': 'time',  # HTML5 time input
                # 'min': '08:00',
                # 'max': '18:00',
                'class': 'form-control',
                'placeholder': 'Select a date first',
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',  # HTML5 date input
                'class': 'form-control',
                'min': datetime.now().date(),
                'placeholder': 'Select a date',
                'onchange': 'onchange_date(this.value)'
            }),
            'service': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select a service',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0',
                'placeholder': 'Price',
            }),
        }
        labels = {
            'service': 'Service',
            'price': 'Price',
            'date': 'Date',
            'time': 'Time',
        }
