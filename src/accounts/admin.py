from django.contrib import admin

from .models        import User, GuestEmail, OwnUser
#from product.models import Product

admin.site.register(User)
admin.site.register(GuestEmail)
admin.site.register(OwnUser)