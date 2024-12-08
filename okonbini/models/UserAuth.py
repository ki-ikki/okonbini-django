from django.db import models

class UserAuth(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.DO_NOTHING,
        null=False
    )
    identity_type = models.CharField(max_length=50, null=False)
    password = models.TextField(null=False)
    token = models.TextField(null=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        # managed = False
        db_table = 'user_auth'

    def __str__(self):
        return f'{self.user} / {self.identity_type}'