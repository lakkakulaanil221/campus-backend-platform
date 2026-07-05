import pytest
from rest_framework.exceptions import ValidationError

from apps.authentication.serializers import RegisterSerializer
from apps.authentication.services import AuthenticationService
from apps.users.models import CustomUser

@pytest.mark.django_db
class TestRegisterSerializer:
    def test_valid_payload(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }

        serializer= RegisterSerializer(data=payload)
        assert serializer.is_valid()
    
    def test_email_required(self):
        payload= {
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }

        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "email" in serializer.errors

    def test_email_invalid(self):
        payload= {
            "email": "johnexample.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "email" in serializer.errors

    def test_username_required(self):
        payload= {
            "email": "john@example.com",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }

        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "username" in serializer.errors

    def test_password_required(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }

        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "password" in serializer.errors

    def test_confirm_password_required(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }

        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "confirm_password" in serializer.errors

    def test_first_name_required(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }

        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "first_name" in serializer.errors

    def test_last_name_required(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "phone_number": "9876543210"
        }

        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "last_name" in serializer.errors

    def test_phone_number_required(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe"
        }
        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "phone_number" in serializer.errors

    def test_passwords_must_match(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@789",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "password" in serializer.errors

    def test_phone_number_10digits_length(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "98765"
        }
        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "phone_number" in serializer.errors

    def test_phone_number_must_be_numeric(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "987654c21a"
        }
        serializer= RegisterSerializer(data=payload)
        assert not serializer.is_valid()
        assert "phone_number" in serializer.errors

@pytest.mark.django_db
class TestAuthenticationService:
    def test_register_new_user(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        user = AuthenticationService.create_user(payload)
        assert user.email == payload["email"]
        assert user.username == payload["username"]
        assert user.is_active == True

    def test_password_is_hashed(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        user = AuthenticationService.create_user(payload)
        assert user.password != payload["password"]
        assert user.check_password(payload["password"])

    def test_password_invalid_length(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Pass",
            "confirm_password": "Pass",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload)
        assert "password" in excinfo.value.detail
        assert "at least 8 characters" in str(excinfo.value.detail["password"][0])

    def test_password_invalid_uppercase(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "password@123",
            "confirm_password": "password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload)
        assert "password" in excinfo.value.detail
        assert "at least one uppercase" in str(excinfo.value.detail["password"][0])

    def test_password_invalid_lowercase(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "PASSWORD@123",
            "confirm_password": "PASSWORD@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload)
        assert "password" in excinfo.value.detail
        assert "at least one lowercase" in str(excinfo.value.detail["password"][0])

    def test_password_invalid_numeric(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "PASSWORd@",
            "confirm_password": "PASSWORd@",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload)
        assert "password" in excinfo.value.detail
        assert "at least one digit" in str(excinfo.value.detail["password"][0])
        
    def test_password_invalid_special_character(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "PASSWORd123",
            "confirm_password": "PASSWORd123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload)
        assert "password" in excinfo.value.detail
        assert "at least one special character" in str(excinfo.value.detail["password"][0])

    def test_password_invalid_spaces(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": " PASSWORd@123",
            "confirm_password": " PASSWORd@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload)
        assert "password" in excinfo.value.detail
        assert "must not contain spaces" in str(excinfo.value.detail["password"][0])

    def test_duplicate_email(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        AuthenticationService.create_user(payload)
        
        payload_duplicate= {
            "email": "john@example.com",
            "username": "john_doe_2",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "Jane",
            "last_name": "Doe",
            "phone_number": "9876543211"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload_duplicate)
        assert "email" in excinfo.value.detail
        assert "Email already exists" in str(excinfo.value.detail["email"][0])

    def test_duplicate_username(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        AuthenticationService.create_user(payload)
        
        payload_duplicate= {
            "email": "jane@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "Jane",
            "last_name": "Doe",
            "phone_number": "9876543211"
        }
        with pytest.raises(ValidationError) as excinfo:
            AuthenticationService.create_user(payload_duplicate)
        assert "username" in excinfo.value.detail
        assert "Username already exists" in str(excinfo.value.detail["username"][0])

    def test_created_at_populated_automatically(self):
        payload= {
            "email": "john@example.com",
            "username": "john_doe",
            "password": "Password@123",
            "confirm_password": "Password@123",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "9876543210"
        }
        user = AuthenticationService.create_user(payload)
        assert user.created_at is not None

    # def test_updated_at_populated_automatically(self):
    #     payload= {
    #         "email": "john@example.com",
    #         "username": "john_doe",
    #         "password": "Password@123",
    #         "confirm_password": "Password@123",
    #         "first_name": "John",
    #         "last_name": "Doe",
    #         "phone_number": "9876543210"
    #     }
    #     user = AuthenticationService.create_user(payload)
    #     assert user.updated_at is not None



