from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class JwtBackend:

    """
        Auth backend utilizing a form of jwt that signs with a key found on the server publicly

        only one user exists

        if user and pass are right -> create token -> when checking permissions check if token is valid -> check role
        need to generate token with User:role signed by pub key

    """

    def authenticate(self, request, username=None, password=None):
        None
