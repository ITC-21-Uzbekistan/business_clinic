from django.urls import path, include

urlpatterns = [
    path('category-employee/', include('apps.category_employee.urls')),
    path('direction-medicine/', include('apps.direction.urls')),
    path('service/', include('apps.service.urls')),
    path('accounting/', include('apps.accounting.urls')),
]