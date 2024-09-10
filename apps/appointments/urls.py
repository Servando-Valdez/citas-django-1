from django.urls import path
from .views import (
    AppointmentIndexView
)

app_name="appointments"

urlpatterns = [
    path('', AppointmentIndexView.as_view(), name="index"),
]