from django.urls import path

from apps.direction.api.business.direction_view import DirectionMedicineListCreateAPIView, \
    DirectionMedicineRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('business/', DirectionMedicineListCreateAPIView.as_view()),
    path('business/<str:pk>/', DirectionMedicineRetrieveUpdateDestroyAPIView.as_view()),
]
