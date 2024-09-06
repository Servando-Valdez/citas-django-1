from django.forms import DateTimeInput, DateInput
import django_filters
from .models import Services

services_fields = {
    "name": {"label": "Name"},
    "price": {"label": "Price"},
}

class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Services
        fields = list(services_fields.keys())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.get_fields():
            self.filters[field_name].label = services_fields[field_name]["label"]
            self.filters[field_name].field.widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": services_fields[field_name]["label"],
                }
            )

            # If it's an input field, change it so that it uses contains
            if self.filters[field_name].__class__.__name__ == "CharFilter":
                self.filters[field_name].lookup_expr = "icontains"