from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .services import AuthenticationService


class RegisterAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = AuthenticationService.create_user(serializer.validated_data)

            return Response(
                {
                    "success": True,
                    "message": "User registered successfully.",
                    "data": {
                        "id": str(user.id),
                        "email": user.email,
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "phone_number": user.phone_number,
                        "is_active": user.is_active,
                        "created_at": user.created_at,
                    },},status=status.HTTP_201_CREATED,
            )

        except ValidationError as exception:
            return Response(
                {
                    "success": False,
                    "message": "Validation failed.",
                    "errors": exception.detail,
                },status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as exception:
            return Response(
                {
                    "success": False,
                    "message": "Internal server error.",
                    "errors": {},
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        
class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        # Implement login logic here
        serializer= LoginSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            JwtToken= AuthenticationService.login(serializer.validated_data)

            #update the below code
            return Response(
                {
                    "success": True,
                    "message": "Login successful.",
                    "data": {
                        "access_token": str(JwtToken.access_token),
                    },
                },
                status=status.HTTP_200_OK,
            )
        
        except ValidationError as exception:
            return Response(
                {
                    "success": False,
                    "message": "Validation failed.",
                    "errors": exception.detail,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        except Exception as exception:
            return Response(
                {
                    "success": False,
                    "message": "Internal server error.",
                    "errors": {},
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer= ChangePasswordSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            AuthenticationService.change_password(request.user, serializer.validated_data)
            return Response(
                {
                    "success": True,
                    "message": "Password changed successfully.",
                    "data": {},
                },
                status=status.HTTP_200_OK,
            )
        
        except ValidationError as exception:
            return Response(
                {
                    "success": False,
                    "message": "Validation failed.",
                    "errors": exception.detail,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as exception:
            return Response(
                {
                    "success": False,
                    "message": "Internal server error.",
                    "errors": {},
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )