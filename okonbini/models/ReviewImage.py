from django.db import models

class ReviewImage(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.DO_NOTHING,
        null=False
    )
    review_image_url = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        # managed = False
        db_table = 'review_images'

    def __str__(self):
        return f'{self.review} / {self.review_image_url}'