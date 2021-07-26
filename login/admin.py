from django.contrib import admin
from .models import User

# Register your models here.
admin.site.register(User)


class user(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'is_Hopstial_admin')
