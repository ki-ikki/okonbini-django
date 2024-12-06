from django.db import models
from django.utils.timezone import now

class StoreLogo(models.Model):
    store = models.OneToOneField(
        'Store',
        on_delete=models.DO_NOTHING,
    )
    store_image_url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'store_logos'

    def __str__(self):
        return f'{self.store} / {self.store_image_url}'

    def createStoreLogo(
        store,
        store_image_url,
        ):
            storeLogo = StoreLogo.objects.create(
                store = store,
                store_image_url = store_image_url,
                created_at = now(),
                updated_at=now(),
            )
            return storeLogo