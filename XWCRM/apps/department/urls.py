from django.urls import path
from .views import DepartmentAPIView


urlpatterns = [
    path("",DepartmentAPIView.as_view()),
]