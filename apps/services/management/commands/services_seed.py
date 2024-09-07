from django.core.management.base import BaseCommand, CommandError
from apps.services.models import Services


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def handle(self, *args, **options):
        run_seed()
        self.stdout.write(self.style.SUCCESS("Seeded Services successfully"))

def run_seed():
    create_services()

def create_services():
    for i in range(1, 100):
        Services.objects.get_or_create(
            name=f"Service {i}",
            description=f"Description {i}",
            price=10.00 * i
        )