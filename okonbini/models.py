from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Contacts(models.Model):
    user_id = models.IntegerField()
    email = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'

class Favorites(models.Model):
    item_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorites'


class Follows(models.Model):
    follower_user_id = models.IntegerField()
    followee_user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follows'


class ItemCategories(models.Model):
    category_name = models.CharField(unique=True, max_length=255)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_categories'


class ItemImages(models.Model):
    item_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_images'


class ItemRatings(models.Model):
    item_id = models.IntegerField()
    store_id = models.IntegerField()
    favorite_weekly_count = models.IntegerField(blank=True, null=True)
    favorite_monthly_count = models.IntegerField(blank=True, null=True)
    favorite_total_count = models.IntegerField(blank=True, null=True)
    review_weekly_count = models.IntegerField(blank=True, null=True)
    review_monthly_count = models.IntegerField(blank=True, null=True)
    review_total_count = models.IntegerField(blank=True, null=True)
    sort_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_ratings'


class Items(models.Model):
    store_id = models.IntegerField()
    category_id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_info = models.TextField()
    price = models.IntegerField()
    release_date = models.DateField(blank=True, null=True)
    search_vector = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Likes(models.Model):
    review_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'likes'


class ReviewImages(models.Model):
    review_id = models.IntegerField()
    review_image_url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_images'


class Reviews(models.Model):
    user_id = models.IntegerField()
    content = models.TextField()
    reply_review_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class StoreLogos(models.Model):
    store_id = models.IntegerField()
    store_image_url = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_logos'


class Stores(models.Model):
    store_name = models.CharField(max_length=255)
    color_code = models.CharField(max_length=7, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores'


class UserAuth(models.Model):
    user_id = models.IntegerField()
    identity_type = models.CharField(max_length=50)
    password = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_auth'


class Users(models.Model):
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
        managed = False
        db_table = 'users'
