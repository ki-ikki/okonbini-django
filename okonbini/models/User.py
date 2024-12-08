from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=255, null=False)
    email = models.CharField(unique=True, max_length=255, null=False)
    description = models.TextField(null=True)
    profile_image_url = models.CharField(null=True)
    location = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        # managed = False
        db_table = 'users'

    def __str__(self):
        return self.user_name