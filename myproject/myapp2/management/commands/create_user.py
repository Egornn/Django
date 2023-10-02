from django.core.management.base import BaseCommand
from myproject.myapp2.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='John', email='john@example.com',phone=88000553535, address="Red square h. 1"  )
        user.save()
        self.stdout.write(f'{user}')


