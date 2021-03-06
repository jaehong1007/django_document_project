from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    # objects = models.Manager() (숨겨져있는거)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        # through_fields 순서 = (source , target)
        through_fields=('group', 'idol')

    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    recommender = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name} {self.idol.name} ({self.is_active})'
