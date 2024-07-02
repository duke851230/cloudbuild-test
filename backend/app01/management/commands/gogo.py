from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print("------------ start run gogo command ------------")
        print("test whether command run successfully or not.")
