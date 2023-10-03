from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException


class UnauthorizedException(APIException):
    """Exception is raised when no access token is found in the client headers."""

    status_code = 401
    default_detail = "Unauthorized"
    default_code = "access_unauthorized"


class ForbiddenException(APIException):
    """Exception raised when access to a resource is denied."""

    status_code = 403
    default_detail = "Access Denied"
    default_code = "access_denied"


class InstanceDoesNotExistError(ValidationError):
    def __init__(self, message="Instance does not exists", *args, **kwargs):
        super().__init__(message, *args, **kwargs)
