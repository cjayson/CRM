from django.urls import path
from .views import DepartmentAPIView,DepartmentSearchAPIView


urlpatterns = [
    path("",DepartmentAPIView.as_view()),
    path("search/",DepartmentSearchAPIView.as_view())
]