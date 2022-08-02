from django.urls import path

from apps.service.api.business import ServiceListCreateAPIView, ServiceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('business/', ServiceListCreateAPIView.as_view()),
    path('business/<str:pk>/', ServiceListCreateAPIView.as_view()),
]