from django.db import models

class Favorite(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete=models.DO_NOTHING,
        null=False
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        # managed = False
        db_table = 'favorites'

    def __str__(self):
        return f'{self.user} / {self.item}'