from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from apps.users.models import CustomUser
from .validators import AuthenticationValidators
from .selectors import AuthenticationSelectors
from rest_framework_simplejwt.tokens import RefreshToken


class AuthenticationService:
    """
    Business logic for Authentication APIs.
    """

    @staticmethod
    def create_user(validated_data):
        # Remove non-model field
        validated_data.pop("confirm_password")

        # Business validations
        AuthenticationValidators.validate_password_policy(
            validated_data["password"]
        )

        try:
            user = CustomUser.objects.create_user(**validated_data)

        except IntegrityError as exception:
            error_message = str(exception).lower()

            if "email" in error_message:
                raise ValidationError({"email": ["Email already exists."]})

            if "username" in error_message:
                raise ValidationError({"username": ["Username already exists."]})

            raise ValidationError({"detail": ["Unable to create user."]}) from exception
        return user
    
    @staticmethod
    def login(validated_data):
        #Authenticate user with email and password
        user= AuthenticationSelectors.authenticate_user(validated_data["email"], validated_data["password"])
        if user is not None:
            #check if user is active
            if not user.is_active:
                raise ValidationError({"detail": ["User account is inactive."]})
            
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return refresh
        raise ValidationError({"detail": ["Invalid credentials."]})
    
    @staticmethod
    def change_password(user, validated_data):
        # Check if current password is correct
        user_authenticated = AuthenticationSelectors.verify_current_password(user, validated_data["current_password"])
        if not user_authenticated:
            raise ValidationError({"detail": ["Current password is incorrect."]})
        # Business validations
        AuthenticationValidators.validate_password_policy(
            validated_data["new_password"]
        )
        if validated_data["current_password"] == validated_data["new_password"]:
            raise ValidationError({"detail": "New password cannot be the same as the current password."})
        # Update user's password
        user.set_password(validated_data["new_password"])
        user.save()
