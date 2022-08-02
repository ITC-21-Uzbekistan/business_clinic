from django.urls import path

from apps.accounting.api.business import AccountingListCreateAPIView, AccountingRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('business/', AccountingListCreateAPIView.as_view()),
    path('business/<str:pk>/', AccountingRetrieveUpdateDestroyAPIView.as_view())
]