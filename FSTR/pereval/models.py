from django.db import models


class User(models.Model):
    """Класс модели пользователя"""
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=12)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Coords(models.Model):
    """Класс модели координат перевала"""
    latitude = models.DecimalField(verbose_name='Latitude', max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(verbose_name='Longitude', max_digits=9, decimal_places=6, null=True)
    height = models.IntegerField(verbose_name='Height', null=True)


