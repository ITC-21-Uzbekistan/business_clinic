from django.urls import path

from apps.category_employee.api.business import CategoryEmployeeListCreateAPIView, \
    CategoryEmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('business/category-employee/', CategoryEmployeeListCreateAPIView.as_view()),
    path('business/category-employee/<str:pk>/', CategoryEmployeeRetrieveUpdateDestroyAPIView),
]
