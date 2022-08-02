from django.urls import path, include

urlpatterns = [
    path('category_employee/', include('apps.category_employee.urls')),
    # path('direction/', include('apps.direction.urls')),
    # path('service/', include('apps.service.urls')),
]