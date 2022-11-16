from login.models import Aspirante
from django.contrib.auth.backends import ModelBackend

"""
    Login via email
"""
class AuthByEmailBackend(ModelBackend):

    def authenticate(username=None, password=None, **kwargs):
        try:
            user = Aspirante.objects.get(email=username)
            if user.check_password(password):
                return user
        except Aspirante.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Aspirante.objects.get(pk=user_id)
        except Aspirante.DoesNotExist:
            return None