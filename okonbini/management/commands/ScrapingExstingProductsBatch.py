from django.core.management.base import BaseCommand
import okonbini.service.SevenElevenService as SevenElevenService

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('テスト用のコマンドバッチを実行しました')
        SevenElevenService.scrapingSevenElevenExistingProducts()