# Create your models here.
from django.db import models


class Doctor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    Address = models.CharField(max_length=150)

    def __str__(self):
        return self.name
