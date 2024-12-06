from django.test import TestCase
from okonbini.models.StoreLogo import StoreLogo
from tests.models.factories import createTestStore

class CreateStoreLogoTestCase(TestCase):
    def setUp(self):
        pass

    def testCreateStoreLogoSuccess(self):
        """正常系: ストアロゴが正常に作成される"""
        store = createTestStore()
        storeImageUrl = "https://test.com/test.jpg"

        storeLogo = StoreLogo.createStoreLogo(
            store,
            storeImageUrl
        )

        self.assertIsNotNone(storeLogo.id)
        self.assertEqual(storeLogo.store, store)
        self.assertEqual(storeLogo.store_image_url, storeImageUrl)
        self.assertIsNotNone(storeLogo.created_at)
        self.assertIsNotNone(storeLogo.updated_at)