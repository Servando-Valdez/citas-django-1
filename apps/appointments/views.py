from typing import Any
from django.shortcuts import render
#Import login required mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Appointment
from .filters import AppointmentFilter
# Create your views here.

class AppointmentIndexView(LoginRequiredMixin, FilterView):
    model = Appointment
    template_name = "appointments/index.html"
    filterset_class = AppointmentFilter
    paginate_by = 10
    context_object_name = "appointments"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Appointments"
        return context
