from rest_framework import serializers
from apps.users.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password= serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ( 'username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'confirm_password')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'confirm_password': {'write_only': True, 'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'phone_number': {'required': True}
            }
    
    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Phone number must be a 10-digit number.")
        return value
    
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "Password and confirm password didn't match."})
        return attrs
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"new_password": "New password and confirm password didn't match."})
        return attrs