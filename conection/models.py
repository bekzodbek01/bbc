from django.db import models


class Conection(models):
    title = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()

