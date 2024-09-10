from django.db import models

# Create your models here.
from django.db import models
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