import uuid

from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, PermissionsMixin):
    GENDER_CHO0ICE = (
        ('male', 'male'),
        ('female', 'female'),
    )
    REGION_CHOICE = (
        ('Tashkent', 'Tashkent'),
        ('Tashkent region', 'Tashkent region'),
        ('Andijan', 'Andijan'),
        ('Bukhara', 'Bukhara'),
        ('Fergana', 'Fergana'),
        ('Jizzakh', 'Jizzakh'),
        ('Xorazm', 'Xorazm'),
        ('Namangan', 'Namangan'),
        ('Navoiy', 'Navoiy'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Samarkand', 'Samarkand'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Surxondaryo', 'Surxondaryo'),
    )
    objects = UserManager()

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    profile_image = models.ImageField(
        upload_to='profile_images/',
        max_length=255,
        blank=True,
        null=True
    )

    username = models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHO0ICE,
        null=True,
        blank=True
    )

    region = models.CharField(
        max_length=50,
        choices=REGION_CHOICE,
        null=True,
        blank=True
    )

    phone = models.PositiveBigIntegerField(
        null=True,
        blank=True
    )

    passport = models.ImageField(
        upload_to='passports/',
        null=True,
        blank=True
    )

    category_employee = models.ForeignKey(
        'CategoryEmployee',  # Need change
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = ["username"]

    class Meta:
        db_table = 'user'
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ['id']

    @property
    def photo_url(self):
        try:
            return self.profile_image.url
        except Exception as e:
            print(e)
            return ''
