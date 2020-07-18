from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

SKILLS = (('transport', 'cat transportation'),
          ('injections', 'making injections'),
          ('pills', 'giving pills'),
          ('photos', 'taking photos'))

AVAILABILITY = (('m08', 'Monday, 8:00 - 9:59'),
                ('m10', 'Monday, 10:00 - 11:59'),
                ('m12', 'Monday, 12:00 - 13:59'),
                ('m14', 'Monday, 14:00 - 15:59'),
                ('m16', 'Monday, 16:00 - 17:59'),
                ('m18', 'Monday, 18:00 - 19:59'),
                ('m20', 'Monday, 20:00 - 21:59'),
                ('t08', 'Tuesday, 8:00 - 9:59'),
                ('t10', 'Tuesday, 10:00 - 11:59'),
                ('t12', 'Tuesday, 12:00 - 13:59'),
                ('t14', 'Tuesday, 14:00 - 15:59'),
                ('t16', 'Tuesday, 16:00 - 17:59'),
                ('t18', 'Tuesday, 18:00 - 19:59'),
                ('t20', 'Tuesday, 20:00 - 21:59'),
                ('w08', 'Wednesday, 8:00 - 9:59'),
                ('w10', 'Wednesday, 10:00 - 11:59'),
                ('w12', 'Wednesday, 12:00 - 13:59'),
                ('w14', 'Wednesday, 14:00 - 15:59'),
                ('w16', 'Wednesday, 16:00 - 17:59'),
                ('w18', 'Wednesday, 18:00 - 19:59'),
                ('w20', 'Wednesday, 20:00 - 21:59'),
                ('th08', 'Thursday, 8:00 - 9:59'),
                ('th10', 'Thursday, 10:00 - 11:59'),
                ('th12', 'Thursday, 12:00 - 13:59'),
                ('th14', 'Thursday, 14:00 - 15:59'),
                ('th16', 'Thursday, 16:00 - 17:59'),
                ('th18', 'Thursday, 18:00 - 19:59'),
                ('th20', 'Thursday, 20:00 - 21:59'),
                )


class UserManager(BaseUserManager):
    def create_user(
            self, email, first_name, last_name, district='', skills=(), phone='', availability=(), password=None,
            commit=True):
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not first_name:
            raise ValueError(_('Users must have a first name'))
        if not last_name:
            raise ValueError(_('Users must have a last name'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            availability=availability,
            district=district,
            skills=skills
        )
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            commit=False,
            )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=150)
    phone = models.CharField(_('phone'), max_length=14)
    availability = MultiSelectField(choices=AVAILABILITY)                  # how to do week days and hours object?
    district = models.CharField(_('district'), max_length=30)
    skills = MultiSelectField(choices=SKILLS)

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
