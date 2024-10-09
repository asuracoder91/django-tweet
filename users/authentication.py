from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .models import User


class UsernameAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get("X-USERNAME")
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("해당 사용자가 존재하지 않습니다.")
        return (user, None)
