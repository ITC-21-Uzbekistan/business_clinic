from django.contrib import admin

from apps.category_employee.models import CategoryEmployee


@admin.register(CategoryEmployee)
class CategoryEmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]
