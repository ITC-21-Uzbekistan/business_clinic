from django.contrib import admin

from auth_user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'is_admin',
        'date_of_birth',
        'profile_image',
        'gender',
        'region',
        'phone',
        'passport',
        'category_employee',
    )
