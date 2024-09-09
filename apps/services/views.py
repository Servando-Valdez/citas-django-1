from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
#import success message
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from .models import Services
from .filters import ServiceFilter
from .forms import ServiceForm
# Create your views here.

class ServicesIndexView(LoginRequiredMixin, FilterView):
    model = Services
    template_name = 'services/index.html'
    context_object_name = 'services'
    filterset_class = ServiceFilter
    paginate_by = 10
    # filterset_fields = ['name']
    # ordering = ['name']
    # search_fields = ['name']

class ServicesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Services
    template_name = 'services/create.html'
    form_class = ServiceForm
    success_url = reverse_lazy('services:index')
    success_message = 'Service was created successfully'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Service'
        return context

class ServicesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Services
    template_name = 'services/create.html'
    form_class = ServiceForm
    success_url = reverse_lazy('services:index')
    success_message = 'Service was updated successfully'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Service'
        return context
    
class ServicesDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Services
    success_url = reverse_lazy('services:index')
    success_message = 'Service was deleted successfully'