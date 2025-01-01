from django.db import models

class Contact(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.DO_NOTHING,
    )
    email = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'contacts'

    def __str__(self):
        return f'{self.email} / {self.content}'