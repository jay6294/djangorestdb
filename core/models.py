from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extraa_fields):
        """create and saves new user"""
        if not email:
            raise ValueError("email field is required ")
        user = self.model(email=self.normalize_email(email), **extraa_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and save new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of user name"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    contactno = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    object = UserManager()
    USERNAME_FIELD = 'email'
