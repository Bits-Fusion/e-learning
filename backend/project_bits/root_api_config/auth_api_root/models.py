from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
    )
from django.utils.translation import gettext_lazy as _


from core_setting.settings import HOSTNAME



class AuthUserAccountManager(BaseUserManager):
    """
    Custome user manager class to creat user and super users.
    """
    def create_user(self, email, user_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email adress'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('You are not a staff mamber')
        return self.create_user(email, user_name, password, **other_fields)
    
    
    def create_admin_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email adress'))
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', False)
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class AuthUserModel(AbstractBaseUser, PermissionsMixin):
    """
    Main user class model.
    Can be extended to companes desire by add or removing different fields to the user model class.
    """
    
    user_name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    # profile_picture = models.ImageField(upload_to='')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(max_length=200, default="male", choices=(('male','male'), ('female','female')))
    age = models.IntegerField(default=0)
    premium_user = models.BooleanField(default=False)
    
    objects = AuthUserAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.user_name
        

    @property
    def get_update_path(self):
        return f'{HOSTNAME}api_root/profile/update/'