from django.db import models


# Create your models here.
class Coffee(models.Model):
    name = models.CharField(default="", max_length=30)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=True)

    def __str__(self):
        return self.name
