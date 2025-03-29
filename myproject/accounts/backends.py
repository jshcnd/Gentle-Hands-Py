from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the username is an email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # If not an email, check if it's a username
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        # Verify the password
        if user.check_password(password):
            return user
        return None