from django.db import models

class Review(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        null=False
    )
    content = models.TextField(null=True)
    reply_review_id = models.IntegerField(null=True)
    item_id = models.ForeignKey(
        'Item',
        on_delete=models.DO_NOTHING,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        # managed = False
        db_table = 'reviews'

    def __str__(self):
        return f'{self.user} / {self.item_id}'