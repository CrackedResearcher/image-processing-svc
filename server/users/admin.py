from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your custom model using the standard UserAdmin logic
admin.site.register(CustomUser, UserAdmin)