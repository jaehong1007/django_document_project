from django.db import models


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField
    members = models.ManyToManyField(Idol)

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(Idol)
    group = models.ForeignKey(Group)
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name} {self.idol.name} ({self.is_active})'
