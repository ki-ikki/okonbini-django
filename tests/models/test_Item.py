from django.test import TestCase
from okonbini.models.Item import Item
from .factories import createTestStore, createTestCategory,createTestItemImage

class CreateItemTestCase(TestCase):
    def setUp(self):
        pass

    def testCreateItemSuccess(self):
        """正常系: アイテムが正常に作成される"""
        store = createTestStore()
        itemCategory = createTestCategory()
        itemImage = createTestItemImage()
        itemName = "Test Item"
        itemInfo = "This is a test item."
        price = 1000
        releaseDate = "2021-01-01"
        isActive = True

        item = Item.createItem(
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