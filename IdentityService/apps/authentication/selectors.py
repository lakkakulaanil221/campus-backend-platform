from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from apps.users.models import CustomUser
from django.contrib.auth import authenticate

class AuthenticationSelectors:

    @staticmethod
    def authenticate_user(email, password):
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None
        
        user = authenticate(username=user.username, password=password)
        return user
    
    @staticmethod
    def verify_current_password(user, current_password):
        return user.check_password(current_password)
