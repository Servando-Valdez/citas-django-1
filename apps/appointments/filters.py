from .models import Appointment

import django_filters

appointments_fields = {
    "service": {"label": "Service"},
    "date": {"label": "Date"},
}

class AppointmentFilter (django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = list(appointments_fields.keys())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.get_fields():
            self.filters[field_name].label = appointments_fields[field_name]["label"]
            self.filters[field_name].field.widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": appointments_fields[field_name]["label"],
                }
            )

            # If it's an input field, change it so that it uses contains
            if self.filters[field_name].__class__.__name__ == "CharFilter":
                self.filters[field_name].lookup_expr = "icontains"