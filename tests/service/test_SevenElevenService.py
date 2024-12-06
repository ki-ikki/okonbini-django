from django.test import TestCase
from okonbini.service.SevenElevenService import scrapingSevenElevenExistingProducts
from tests.models.factories import createTestStore, createTestItemCategoryList

class TestSevenElevenService(TestCase):
    def test_scraping_function(self):
        createTestStore()
        createTestItemCategoryList()

        # サービス関数を呼び出して結果を取得
        result = scrapingSevenElevenExistingProducts()
