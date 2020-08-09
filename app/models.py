from django.db import models


class Car(models.Model):

    MANUAL = 0
    AUTO = 1
    CVT = 2
    TRANSMISSION_CHOICES = [
        (MANUAL, 'Manual'),
        (AUTO, 'Auto'),
        (CVT, 'CVT')
    ]

    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=18)
    release_year = models.IntegerField()
    transmission = models.SmallIntegerField(
        choices=TRANSMISSION_CHOICES, default=0)

    def __str__(self):
        return f'{self.brand} {self.model} {self.release_year}'

    def get_brands(self):
        return [(v, v) for v in self.brand]
