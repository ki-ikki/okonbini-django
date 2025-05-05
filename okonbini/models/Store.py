from django.db import models
from django.utils.timezone import now

class Store(models.Model):
    SEVEN_ELEVEN = 'seven_eleven'
    LAWSON = 'lawson'
    FAMILY_MART = 'family_mart'

    store_name = models.CharField(max_length=255, null=False)
    store_logical_name = models.CharField(max_length=255, null=False)
    color_code = models.CharField(max_length=7, null=False)
    is_active = models.BooleanField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        # managed = False
        db_table = 'stores'

    def __str__(self):
        return self.store_name

    def createStore(
        store_name,
        store_logical_name,
        colorCode=None,
        isActive=True
        ):
            store = Store.objects.create(
                store_name = store_name,
                store_logical_name = store_logical_name,
                color_code = colorCode,
                is_active = isActive,
                updated_at = now(),
                deleted_at = None
            )
            return store

    def getStoreFromName(storeName):
        return Store.objects.get(store_name = storeName)