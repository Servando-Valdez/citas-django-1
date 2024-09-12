from datetime import datetime, time, timedelta
from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_filters.views import FilterView
from .models import Appointment
from .filters import AppointmentFilter
from .forms import AppointmentForm
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
    
class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = "appointments/create.html"
    form_class = AppointmentForm
    success_url = reverse_lazy("appointments:index")

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Appointment"
        if self.request.htmx:
            selected_date = self.request.GET.get('date')
            if selected_date:
                # Filtrar las horas ocupadas para la fecha seleccionada
                occupied_times = Appointment.objects.filter(date=selected_date).values_list('time', flat=True)
                context['occupied_times'] = occupied_times
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = None
        form = self.get_form()

        if not form.is_valid():
            context = self.get_context_data()
            context["form"] = form
            return render(request, self.template_name, context)

        self.object = form.save()
        messages.success(request, "Appointment was created successfully")
        return HttpResponse(200)
    
def get_occupied_times(request):
    date = request.GET.get('date') 
    date = datetime.strptime(date, '%Y-%m-%d').date()

    if date:
        # Filtrar las citas existentes por la fecha seleccionada
        occupied_appointments = Appointment.objects.filter(date=date).values_list('time', flat=True)
        occupied_times = [appt.strftime("%H:%M") for appt in occupied_appointments]

        # Generar las horas disponibles de 8:00 a 18:00
        start_time = time(8, 0)
        end_time = time(18, 0)
        time_slots = []
        current_time = start_time

        while current_time < end_time:
            time_str = current_time.strftime("%H:%M")
            if time_str not in occupied_times:
                time_slots.append(time_str)
            current_time = (datetime.combine(date.today(), current_time) + timedelta(minutes=60)).time()

        return JsonResponse({'available_times': time_slots})

    return JsonResponse({'error': 'No date provided'}, status=400)