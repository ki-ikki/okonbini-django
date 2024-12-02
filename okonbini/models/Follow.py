from django.db import models

class Follow(models.Model):
    follower_user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        related_name='follower_user',
    )
    followee_user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        related_name='followee_user',
    )
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'follows'