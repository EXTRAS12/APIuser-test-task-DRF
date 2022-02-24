from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Модель кастомного юзера"""
    other_name = models.CharField('Другое имя', max_length=100, default='')
    phone = models.CharField('Номер телефона', max_length=100)
    birthday = models.DateField('Дата рождения', default='1992-10-05')
    city = models.ForeignKey('City', on_delete=models.PROTECT, null=True,
                             blank=True, max_length=100)
    additional_info = models.CharField('Дополнительная информация', max_length=255)
    is_admin = models.BooleanField(default=True)


class City(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
