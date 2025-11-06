from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from account.manager import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    phone_number = models.CharField(
        max_length=11, unique=True, verbose_name="شماره تلفن",
    )
    email = models.EmailField(_('ایمیل'), null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    is_owner = models.BooleanField(_('مالک هست؟'), default=False)
    is_superuser = models.BooleanField(_('ادمین هست؟'), default=False)
    is_active = models.BooleanField(_('فعال'), default=True)
    is_staff = models.BooleanField(_('کارمند'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.phone_number

