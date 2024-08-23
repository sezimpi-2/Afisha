from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
import random

class User(AbstractUser):
    is_active = models.BooleanField(default=False)  # Пользователь неактивен по умолчанию

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        super().save(*args, **kwargs)
