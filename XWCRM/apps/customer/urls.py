from django.urls import path
from .views import PublicCustomerAPIView,CustomerAPIView

urlpatterns = [
    path("", CustomerAPIView.as_view()),
    path("public/", PublicCustomerAPIView.as_view()),
]
