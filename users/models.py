from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail


JOB_ROLES = (
    # ('_database_', '_visible_'),
    ('SUPPLIER', 'JR1'),
    ('COMPANY', 'JR2'),
    ('admin', 'JR3'),
    ('employee', 'JR4'),
)

USER_TYPES = (
    ('admin', 'Admin'),
    ('employee', 'Employee'),
)


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, error_messages={
                                  'unique': "A user with that email already exists.",
                                },
                                )
    email = models.EmailField(unique=True,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              },
                              )

    job_role = models.CharField(max_length=50, null=True, choices=JOB_ROLES)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, null=True, choices=USER_TYPES)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)