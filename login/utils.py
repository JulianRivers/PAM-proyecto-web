from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, Aspirante, timestamp):
        return (six.text_type(Aspirante.pk)+six.text_type(timestamp)+six.text_type(Aspirante.is_email_verified))


generate_token =TokenGenerator()