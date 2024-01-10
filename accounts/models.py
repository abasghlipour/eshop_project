from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import UserManager


# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='ایمیل')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیر فعال')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین/معمولی')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11,unique=True)
    code = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'

    class Meta:
        verbose_name = 'کد احراز هویت'
        verbose_name_plural = 'کدهای احراز هویت'
