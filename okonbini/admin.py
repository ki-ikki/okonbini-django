from django.contrib import admin
from .models import Contacts
from .models import Favorites
from .models import Follows
from .models import ItemCategories
from .models import ItemImages
from .models import ItemRatings
from .models import Items
from .models import Likes
from .models import ReviewImages
from .models import Reviews
from .models import StoreLogos
from .models import Stores
from .models import UserAuth
from .models import Users

# Register your models here.
admin.site.register(Contacts)
admin.site.register(Favorites)
admin.site.register(Follows)
admin.site.register(ItemCategories)
admin.site.register(ItemImages)
admin.site.register(ItemRatings)
admin.site.register(Items)
admin.site.register(Likes)
admin.site.register(ReviewImages)
admin.site.register(Reviews)
admin.site.register(StoreLogos)
admin.site.register(Stores)
admin.site.register(UserAuth)
admin.site.register(Users)