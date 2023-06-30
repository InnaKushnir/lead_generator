from django.contrib import admin


from .models import (
    User,
    Object
)

admin.site.register(User)
admin.site.register(Object)
