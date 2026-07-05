from django.urls import path
from .views import *

#app_name = "authentication"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("change-password/", ChangePasswordAPIView.as_view(), name="change_password"),
]
