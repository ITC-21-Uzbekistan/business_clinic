from django.urls import path

from apps.category_employee.api.business import CategoryEmployeeListCreateAPIView, \
    CategoryEmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('business/', CategoryEmployeeListCreateAPIView.as_view()),
    path('business/<str:pk>/', CategoryEmployeeRetrieveUpdateDestroyAPIView.as_view()),
]
