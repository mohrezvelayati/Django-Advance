from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', {
            'fields':(
                'email', 'password'
            ),
        }),
        ('Permissions', {
            'fields':(
                'is_staff', 'is_active', 'is_superuser'
            ),
        }),
        ('Group Permissions', {
            'fields':(
                'groups', 'user_permissions',
            ),
        }),
        ('Important Dates', {
                'fields':(
                    'last_login',
                ),
            }),
    ) 
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)