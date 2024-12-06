from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
    )
    email = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'contacts'

    def __str__(self):
        return f'{self.email} / {self.content}'