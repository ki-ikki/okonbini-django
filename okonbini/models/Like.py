from django.db import models

class Like(models.Model):
    review = models.ForeignKey(
        'Review',
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
        db_table = 'likes'

    def __str__(self):
        return f'{self.user} / {self.review}'