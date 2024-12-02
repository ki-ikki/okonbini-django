from django.db import models

class Review(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
    )
    content = models.TextField()
    reply_review_id = models.IntegerField(blank=True, null=True)
    item_id = models.ForeignKey(
        'Item',
        on_delete=models.DO_NOTHING,
    )
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'reviews'