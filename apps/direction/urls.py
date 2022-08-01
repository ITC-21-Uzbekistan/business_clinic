from django.urls import path

from apps.direction.api.business.category_employee_view import DirectionMedicineListCreateAPIView, \
    DirectionMedicineRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('business/direction-medicine/', DirectionMedicineListCreateAPIView.as_view()),
    path('business/direction-medicine/<str:pk>/', DirectionMedicineRetrieveUpdateDestroyAPIView.as_view()),
]
