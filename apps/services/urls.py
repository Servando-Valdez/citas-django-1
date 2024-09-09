from django.urls import path
from .views import ServicesIndexView, ServicesCreateView


app_name="services"

urlpatterns = [
    path('', ServicesIndexView.as_view(), name="index"),
    path('create/', ServicesCreateView.as_view(), name="create"),
]
