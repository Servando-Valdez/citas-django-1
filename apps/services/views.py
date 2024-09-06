from django.shortcuts import render
#import loginrequiredmixin to class views
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .models import Services
# Create your views here.

class ServicesIndexView(LoginRequiredMixin, FilterView):
    model = Services
    template_name = 'services/index.html'
    context_object_name = 'services'
    paginate_by = 10
    # filterset_fields = ['name']
    # ordering = ['name']
    # search_fields = ['name']

