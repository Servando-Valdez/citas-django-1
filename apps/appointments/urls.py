from django.urls import path
from .views import (
    AppointmentIndexView,
    AppointmentCreateView,
    get_occupied_times
)

app_name="appointments"

urlpatterns = [
    path('', AppointmentIndexView.as_view(), name="index"),
    path('create/', AppointmentCreateView.as_view(), name="create"),
    path('occupied-times/', get_occupied_times, name='get_occupied_times'),
]