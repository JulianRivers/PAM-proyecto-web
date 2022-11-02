from django.contrib.auth.base_user import BaseUserManager

class AspiranteManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        print("hola")
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def get_full_name(self):
        '''  
        Returns the first_name plus the last_name, with a space in between.  
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):  
        '''  
        Returns the short name for the user.  
        '''  
        return self.first_name