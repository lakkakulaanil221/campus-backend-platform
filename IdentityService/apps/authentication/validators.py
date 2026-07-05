import re
from rest_framework.exceptions import ValidationError
#from .selectors import email_exists, username_exists

class AuthenticationValidators:
    """
    Business validation for Authentication APIs.
    """
    @staticmethod
    def validate_password_policy(password: str) -> None:
        if len(password) < 8:
            raise ValidationError({"password": ["Password must contain at least 8 characters."]})

        if not re.search(r"[A-Z]", password):
            raise ValidationError({"password": ["Password must contain at least one uppercase letter."]})

        if not re.search(r"[a-z]", password):
            raise ValidationError({"password": ["Password must contain at least one lowercase letter."]})

        if not re.search(r"\d", password):
            raise ValidationError({"password": ["Password must contain at least one digit."]})

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError({"password": ["Password must contain at least one special character."]})

        if " " in password:
            raise ValidationError({"password": ["Password must not contain spaces."]})


