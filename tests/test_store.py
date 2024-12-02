from django.test import TestCase
from okonbini.models.Store import create_store

class CreateStoreTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_store_success(self):
        """正常系: ストアが正常に作成される"""
        store_name = "Test Store"
        color_code = "#FFFFFF"
        is_active = True

        store = create_store(store_name, color_code, is_active)

        self.assertIsNotNone(store.id)
        self.assertEqual(store.store_name, store_name)
        self.assertEqual(store.color_code, color_code)
        self.assertEqual(store.is_active, is_active)
        self.assertIsNone(store.deleted_at)
        self.assertIsNotNone(store.updated_at)
