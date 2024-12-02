from django.test import TestCase
from okonbini.models.StoreLogo import create_store_logo
from .factories import create_test_store

class CreateStoreLogoTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_store_logo_success(self):
        """正常系: ストアロゴが正常に作成される"""
        store = create_test_store()
        storeImageUrl = "https://test.com/test.jpg"

        storeLogo = create_store_logo(
            store,
            storeImageUrl
        )

        self.assertIsNotNone(storeLogo.id)
        self.assertEqual(storeLogo.store, store)
        self.assertEqual(storeLogo.store_image_url, storeImageUrl)
        self.assertIsNotNone(storeLogo.created_at)
        self.assertIsNotNone(storeLogo.updated_at)