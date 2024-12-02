from django.db import models

class Like(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.DO_NOTHING,
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
    )
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'likes'