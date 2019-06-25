from django.urls import path
from .views import LoginAPIView, RegisterAPIView,StaffListAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view()),
    path("register/", RegisterAPIView.as_view()),
    path("userinfo/",StaffListAPIView.as_view()),
]
