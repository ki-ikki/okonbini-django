from django.test import TestCase
from okonbini.service.SevenElevenService import scrapingSevenElevenExistingProducts, scrapingSevenElevenNewProducts
from tests.models.factories import createTestStore, createTestItemCategoryList

class TestSevenElevenService(TestCase):
    def testScrapingSevenElevenExistingProducts(self):
        """
        セブンイレブンの既存商品をスクレイピングする一連の処理
        """
        createTestStore()
        createTestItemCategoryList()

        scrapingSevenElevenExistingProducts()

    def testScrapingSevenElevenNewProducts(self):
        """
        セブンイレブンの新商品をスクレイピングする一連の処理
        """
        createTestStore()
        createTestItemCategoryList()

        scrapingSevenElevenNewProducts()
