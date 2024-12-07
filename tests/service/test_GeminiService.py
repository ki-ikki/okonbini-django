from django.test import TestCase
import okonbini.service.GeminiService as GeminiService
import tests.models.factories as factories

class TestGeminiService(TestCase):
    def testGetItemCategoryFromItemName(self):
        factories.createTestItemCategoryList()

        itemTitle = '７ＰＬ薄手透け感タイツ　３０Ｄ　Ｍ－Ｌ'
        itemInfo = None

        GeminiService.getItemCategoryFromItemName(itemTitle, itemInfo)