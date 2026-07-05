import pytest

from apps.authentication.serializers import ChangePasswordSerializer
from apps.authentication.services import AuthenticationService
from apps.users.models import CustomUser