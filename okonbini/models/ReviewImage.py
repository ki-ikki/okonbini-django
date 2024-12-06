from django.db import models

class ReviewImage(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.DO_NOTHING,
    )
    review_image_url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'review_images'

    def __str__(self):
        return f'{self.review} / {self.review_image_url}'