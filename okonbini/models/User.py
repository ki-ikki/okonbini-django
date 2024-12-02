from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    profile_image_url = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'users'