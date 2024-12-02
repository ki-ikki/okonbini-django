from django.test import TestCase
from okonbini.models.Item import create_item
from .factories import create_test_store, create_test_category,create_test_item_image

class CreateItemTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_item_success(self):
        """正常系: アイテムが正常に作成される"""
        store = create_test_store()
        itemCategory = create_test_category()
        itemImage = create_test_item_image()
        itemName = "Test Item"
        itemInfo = "This is a test item."
        price = 1000
        releaseDate = "2021-01-01"
        isActive = True

        item = create_item(
            store,
            itemCategory,
            itemImage,
            itemName,
            itemInfo,
            price,
            releaseDate,
            isActive
        )

        self.assertIsNotNone(item.id)
        self.assertEqual(item.store, store)
        self.assertEqual(item.item_category, itemCategory)
        self.assertEqual(item.item_name, itemName)
        self.assertEqual(item.item_info, itemInfo)
        self.assertEqual(item.price, price)
        self.assertEqual(item.release_date, releaseDate)
        self.assertEqual(item.is_active, isActive)
        self.assertIsNotNone(item.created_at)
        self.assertIsNotNone(item.updated_at)