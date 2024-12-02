from django.test import TestCase
from okonbini.models.ItemCategory import create_item_category

class CreateItemCategoryTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_item_category_success(self):
        """正常系: アイテムカテゴリが正常に作成される"""
        itemCategoryName = "Test Category"

        itemCategory = create_item_category(
            itemCategoryName,
        )

        self.assertIsNotNone(itemCategory.id)
        self.assertEqual(itemCategory.category_name, itemCategoryName)
        self.assertTrue(itemCategory.is_active)
        self.assertIsNotNone(itemCategory.created_at)
        self.assertIsNotNone(itemCategory.updated_at)