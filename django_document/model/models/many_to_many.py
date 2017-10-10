from django.db import models

__all__ = (
    'Pizza',
    'Topping',
)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(
        'Topping',
        blank=True,
    )

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class TwitterUser(models.Model):

    # 자기자신(Twitteruser ('self'))를 참조해서
    # friends필드를 MTM으로 정의

    name = models.CharField(max_length=30)
    freinds = models.ManyToManyField('self', blank=True,)

    def __str__(self):
        return self.name
