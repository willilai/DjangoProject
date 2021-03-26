from django.db import models

class Specie(models.Model):
    name = models.CharField(max_length=500)
    numWhales = models.IntegerField(default=0)
    diet = models.CharField(max_length=500)
    size = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    def __str__(self):
        return self.name
