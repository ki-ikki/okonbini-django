from django.db import models

class UserAuth(models.Model):
    user = models.OneToOneField(
        'User',
        on_delete=models.DO_NOTHING,
    )
    identity_type = models.CharField(max_length=50)
    password = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'user_auth'

    def __str__(self):
        return f'{self.user} / {self.identity_type}'