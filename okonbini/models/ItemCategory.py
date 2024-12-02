from django.db import models
from django.utils.timezone import now

class ItemCategory(models.Model):
    category_name = models.CharField(unique=True, max_length=255)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'item_categories'

def create_item_category(itemCategoryName):
    itemCategory = ItemCategory.objects.create(
        category_name=itemCategoryName,
        is_active=True,
        created_at=now(),
        updated_at=now(),
    )
    return itemCategory
