from django.test import TestCase
from okonbini.models.ItemImage import ItemImage

class CreateItemImageTestCase(TestCase):
    def setUp(self):
        pass

    def testCreateItemImageSuccess(self):
        """正常系: アイテム画像が正常に作成される"""
        itemImageUrl = "https://example"

        itemImage = ItemImage.createItemImage(
            itemImageUrl,
        )

        self.assertIsNotNone(itemImage.id)
        self.assertEqual(itemImage.item_image_url, itemImageUrl)
        self.assertIsNotNone(itemImage.created_at)
        self.assertIsNotNone(itemImage.updated_at)