from django.db import models

class Follow(models.Model):
    follower_user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        related_name='follower_user',
        null=False
    )
    followee_user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
        related_name='followee_user',
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'follows'

    def __str__(self):
        return f'{self.follower_user} / {self.followee_user}'