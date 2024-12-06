from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.db.models import F
from django.utils.timezone import now

class Item(models.Model):
    TAX_RATE = 0.1

    store = models.ForeignKey(
        'Store',
        on_delete=models.DO_NOTHING,
    )
    item_category = models.ForeignKey(
        'ItemCategory',
        on_delete=models.DO_NOTHING,
    )
    item_image = models.OneToOneField(
        'ItemImage',
        on_delete=models.DO_NOTHING,
    )
    item_name = models.CharField(max_length=255)
    item_info = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    release_date = models.DateField(blank=True, null=True)
    search_vector = SearchVectorField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'items'

    def __str__(self):
        return f'{self.item_name}({self.item_category.category_name}) / {self.price}'

    def createItem(
        store,
        itemCategory,
        itemImage,
        itemName,
        itemInfo,
        price,
        releaseDate,
        isActive,
        ):

        # 検索用のベクトルを作成
        search_vector = f"{itemName} {itemInfo}"

        item = Item.objects.create(
            store = store,
            item_category = itemCategory,
            item_image = itemImage,
            item_name = itemName,
            item_info = itemInfo,
            price = price,
            release_date = releaseDate,
            search_vector=search_vector,
            is_active = isActive,
            created_at = now(),
            updated_at = now()
        )
        return item