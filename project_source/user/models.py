from __future__ import unicode_literals

import re
import os
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from .managers import UserManager

def profile_image_directory_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'profile/'+re.sub('[-:. ]','',str(datetime.today()))+file_extension


USER_TYPE = (
    ('admin','Admin'),
    ('seller','Seller'),
    ('customer','Customer'),
)

#any change is user model field also need to be changed in forms.py and admin.py
class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(_('email address'), unique=True)
    first_name  = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name   = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    user_type   = models.CharField(max_length=15, choices=USER_TYPE, null=True, blank=True, default='customer')
    is_staff    = models.BooleanField(_('staff'), default=False)
    mobile      = models.CharField(max_length = 15, null = True, blank=True, unique=True)
    dob         = models.DateField(null=True, blank=True)
    is_active   = models.BooleanField(_('active'), default=False)
    avatar      = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_verified = models.BooleanField(_('verified'), default=False)
    objects     = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # def get_full_name(self):
    #     if self.first_name and self.last_name:
    #         full_name = '%s %s' % (self.first_name, self.last_name)
    #     elif self.first_name:
    #         full_name = self.first_name
    #     elif self.last_name:
    #         full_name = self.last_name
    #     else:   #if a user do not have first_name and last_name set send the email
    #         full_name = self.email
    #     return full_name.strip()

    # def get_short_name(self):
    #     if self.first_name: #check if a user have first_name set else send email
    #         return self.first_name
    #     return self.email

    @property#        send_mail(mail_subject, 'Please activate your account', 'noreply.influence@gmail.com', [str(user.email)])
    def is_admin(self):
        if self.user_type == 'admin':
            return True
        else:
            return False

def one_day_hence():
    return timezone.now() + timezone.timedelta(days=1)

class UserToken(models.Model):
    tokenType = (
        (1,('New Account')),
        (2,('Forget Password')),
    )
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    token       = models.TextField(null = True, blank = True)
    token_type  = models.PositiveIntegerField(choices=tokenType, default=1)
    active      = models.BooleanField(default = False)
    created_at  = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField(blank = True, default = one_day_hence)
    expire_date  = models.DateTimeField(blank = True, default = datetime.now() + timedelta(hours=24))

    
# class CompanyProfile(models.Model):
#     user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="company_profile")
#     name        = models.CharField(max_length=100)
#     gst         = models.CharField(max_length = 15, null = True, blank = True)
#     pincode    = models.CharField(max_length = 7)
#     area        = models.CharField(max_length = 100)
#     city        = models.ForeignKey('main.City', on_delete=models.CASCADE, related_name = "company_profile_city")
#     state       = models.ForeignKey('main.State', on_delete=models.CASCADE, related_name = "company_profile_state")
#     country     = models.ForeignKey('main.Country', on_delete=models.CASCADE, related_name = "company_profile_country")
#     address_1   = models.TextField()
#     address_2   = models.TextField(null = True, blank = True)    
#     landmark    = models.CharField(max_length = 100, null = True, blank = True)
#     description = models.TextField(null = True, blank = True)

#     def __str__(self):
#         if self.user.first_name:
#             return self.name+'-'+self.user.first_name
#         else:
#             return self.name

        
# class UserAddress(models.Model):
#     user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses")
#     pincode   = models.CharField(max_length = 7)
#     area      = models.CharField(max_length = 100)
#     city      = models.ForeignKey('main.City', on_delete=models.CASCADE, related_name = "user_address_city")
#     state     = models.ForeignKey('main.State', on_delete=models.CASCADE, related_name = "user_address_state")
#     country   = models.ForeignKey('main.Country', on_delete=models.CASCADE, related_name = "user_address_country")
#     address_1 = models.TextField()
#     address_2 = models.TextField(null = True, blank = True)
#     landmark  = models.CharField(max_length = 100, null = True, blank = True)
#     active    = models.BooleanField(default = True)

#     def __str__(self):
#         return self.user.email

