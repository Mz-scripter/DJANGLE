import json
from django.core.management.base import BaseCommand
from search.models import SearchResult


class Command(BaseCommand):
    help = "Populate the SearchResult table with data from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument()