from django.test import TestCase
from okonbini.models.Store import Store

class CreateStoreTestCase(TestCase):
    def setUp(self):
        pass

    def testCreateStoreSuccess(self):
        """正常系: ストアが正常に作成される"""
        store_name = "Test Store"
        color_code = "#FFFFFF"
        is_active = True

        store = Store.createStore(store_name, color_code, is_active)

        self.assertIsNotNone(store.id)
        self.assertEqual(store.store_name, store_name)
        self.assertEqual(store.color_code, color_code)
        self.assertEqual(store.is_active, is_active)
        self.assertIsNone(store.deleted_at)
        self.assertIsNotNone(store.updated_at)
