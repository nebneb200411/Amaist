from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid


class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    username_validator = UnicodeUsernameValidator()

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    email = models.EmailField('メールアドレス',
                              unique=True,
                              error_messages={
                                  'invalid': "正しいメールアドレスを入力してください．",
                                  'unique': "このメールアドレスは既に登録されています．",
                                  'required': "この項目は必須です．",
                              }
                              )
    username = models.CharField(
        _('username'), unique=True, max_length=50, blank=False,
        help_text='必須の項目です．全角文字，半角英数字，@/./+/-/_ で50文字以下にしてください．',
        validators=[username_validator],
        error_messages={
            'unique': _("入力いただいたユーザー名は既に存在しています．別のをお試しください．"),
        })

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
