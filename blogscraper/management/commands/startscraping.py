from django.core.management.base import BaseCommand
from blogscraper.scraper import scrape_all

class Command(BaseCommand):
    def handle(self, *args, **options):
        scrape_all()
