from django.test import TestCase
from okonbini.models.ItemImage import create_item_image

class CreateItemImageTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_item_image_success(self):
        """正常系: アイテム画像が正常に作成される"""
        itemImageUrl = "https://example"

        itemImage = create_item_image(
            itemImageUrl,
        )

        self.assertIsNotNone(itemImage.id)
        self.assertEqual(itemImage.item_image_url, itemImageUrl)
        self.assertIsNotNone(itemImage.created_at)
        self.assertIsNotNone(itemImage.updated_at)