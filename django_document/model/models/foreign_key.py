from django.db import models

__all__ = (
    'Car',
    'Manufacturer',
    'User',
)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'


class User(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

