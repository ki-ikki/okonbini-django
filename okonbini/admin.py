from django.contrib import admin
from .models.Contact import Contact
from .models.Favorite import Favorite
from .models.Follow import Follow
from .models.ItemCategory import ItemCategory
from .models.ItemImage import ItemImage
from .models.ItemRating import ItemRating
from .models.Item import Item
from .models.Like import Like
from .models.ReviewImage import ReviewImage
from .models.Review import Review
from .models.StoreLogo import StoreLogo
from .models.Store import Store
from .models.UserAuth import UserAuth
from .models.User import User

# Register your models here.
admin.site.register(Contact)
admin.site.register(Favorite)
admin.site.register(Follow)
admin.site.register(ItemCategory)
admin.site.register(ItemImage)
admin.site.register(ItemRating)
admin.site.register(Item)
admin.site.register(Like)
admin.site.register(ReviewImage)
admin.site.register(Review)
admin.site.register(StoreLogo)
admin.site.register(Store)
admin.site.register(UserAuth)
admin.site.register(User)