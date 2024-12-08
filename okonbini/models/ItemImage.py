from django.db import models
from django.utils.timezone import now

class ItemImage(models.Model):
    item_image_url = models.TextField(null=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'item_images'

    def __str__(self):
        return f'{self.item_image_url}'

    def createItemImage(
        itemImageUrl,
        ):
            itemImage = ItemImage.objects.create(
                item_image_url = itemImageUrl,
                created_at = now(),
                updated_at = now(),
            )
            return itemImage