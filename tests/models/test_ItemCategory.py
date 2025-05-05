from django.test import TestCase
from okonbini.models.ItemCategory import ItemCategory

class CreateItemCategoryTestCase(TestCase):
    def setUp(self):
        pass

    def testCreateItemCategorySuccess(self):
        """正常系: アイテムカテゴリが正常に作成される"""
        itemCategoryName = "Test Category"
        itemCategoryLabel = "Test Category Label"

        itemCategory = ItemCategory.createItemCategory(
            itemCategoryName,
            itemCategoryLabel
        )

        self.assertIsNotNone(itemCategory.id)
        self.assertEqual(itemCategory.category_name, itemCategoryName)
        self.assertTrue(itemCategory.is_active)
        self.assertIsNotNone(itemCategory.created_at)
        self.assertIsNotNone(itemCategory.updated_at)