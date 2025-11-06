from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        """
        Create and save a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError(_('باید یک شماره تلفن وارد کنید'))
        
        email = self.normalize_email(email) if email else None
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given phone number and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_owner', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('سوپر یوزر باید is_superuser=True باشد'))
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('سوپر یوزر باید is_staff=True باشد'))

        return self.create_user(phone_number, email, password, **extra_fields)