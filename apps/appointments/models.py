from django.db import models

# Create your models here.
from django.db import models
from django.forms import ValidationError
from django.utils import timezone
from datetime import time
from apps.services.models import Services

class Appointment(models.Model):
    service = models.ForeignKey(Services, on_delete=models.DO_NOTHING) # Field for the service of the appointment
    date = models.DateField()  # Field for the date of the appointment
    time = models.TimeField()  # Field for the time of the appointment
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Field for the price of the appointment
    created_at = models.DateTimeField(auto_now_add=True)  # Time when the appointment was created

    def __str__(self):
        return f"{self.service.name} - {self.date} at {self.time}"

    class Meta:
        unique_together = ('date', 'time')
        db_table = 'appointments'
        ordering = ['date', 'time']
    
    def clean(self):
        # Definir los límites de hora
        if not time(8, 0) <= self.time <= time(18, 0):
            raise ValidationError("The time must be between 8:00 am and 6:00 pm.")
        
        # Chequear si la hora está ocupada
        if Appointment.objects.filter(date=self.date, time=self.time).exists():
            raise ValidationError("There is already an appointment reserved for this date and time.")