from django.contrib import admin
from .models import AuthUserModel as User

admin.site.register(User)