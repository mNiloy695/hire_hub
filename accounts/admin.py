from django.contrib import admin
from .models import CustomUserModel
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(CustomUserModel)
