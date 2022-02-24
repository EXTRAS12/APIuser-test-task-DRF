from django.contrib import admin

from .models import City, CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'username', 'first_name',)
    list_display = ('id', 'username', 'first_name', 'phone', 'birthday',)
    fields = ('username', 'first_name', 'last_name', 'other_name', 'email', 'phone', 'birthday',
              'city', 'additional_info', 'is_admin')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(City)
