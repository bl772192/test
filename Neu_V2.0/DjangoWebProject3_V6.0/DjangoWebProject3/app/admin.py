from django.contrib import admin
from .models import Input
from app.models import UserProfile

admin.site.register(Input)
admin.site.register(UserProfile)