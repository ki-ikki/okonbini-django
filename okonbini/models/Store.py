from django.db import models
from django.utils.timezone import now

class Store(models.Model):
    SEVEN_ELEVEN = 'seven_eleven'
    LAWSON = 'lawson'
    FAMILY_MART = 'family_mart'

    store_name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=7, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'stores'

    def __str__(self):
        return self.store_name

    def createStore(
        store_name,
        colorCode=None,
        isActive=True
        ):
            store = Store.objects.create(
                store_name = store_name,
                color_code = colorCode,
                is_active = isActive,
                updated_at = now(),
                deleted_at = None
            )
            return store

    def getStoreFromName(storeName):
        return Store.objects.get(store_name = storeName)