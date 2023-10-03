from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings

from .exceptions import ForbiddenException, UnauthorizedException


class JWTPermissionValidator:
    """Class for validating JWT permissions."""

    @classmethod
    def validate_jwt_authentication_or_raise(cls, request):
        """Validate JWT token for authentication."""

        jwt_auth = JWTAuthentication()
        header = jwt_auth.get_header(request)
        if not header or not cls._is_valid_auth_type(header):
            raise UnauthorizedException()
        return jwt_auth.authenticate(request)

    @staticmethod
    def _is_valid_auth_type(header):
        """Check the validity of the authentication type"""

        for auth_type in api_settings.AUTH_HEADER_TYPES:
            if header.startswith(auth_type.encode("utf-8")):
                return True
        return False

    @classmethod
    def is_superuser_or_raise(cls, request):
        """Check permission to only allow superuser."""

        user, _ = cls.validate_jwt_authentication_or_raise(request)
        if not user.is_superuser:
            raise ForbiddenException("Only superuser allow.")
