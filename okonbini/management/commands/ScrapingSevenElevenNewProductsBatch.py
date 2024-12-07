from django.core.management.base import BaseCommand
import okonbini.service.SevenElevenService as SevenElevenService

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        SevenElevenService.scrapingSevenElevenNewProducts()