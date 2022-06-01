from django.contrib import admin

from rest_shop.models import CartProduct, Item, LikeProduct

admin.site.register(Item)
admin.site.register(CartProduct)
admin.site.register(LikeProduct)
