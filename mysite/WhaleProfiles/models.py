from django.db import models

class Specie(models.Model):
    name = models.CharField(max_length=200)
    numWhales = models.IntegerField(default=0)
    def __str__(self):
        return self.name
