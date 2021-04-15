from django.db import models

class Specie(models.Model):
    name = models.CharField(max_length=500)
    numWhales = models.IntegerField(default=0)
    diet = models.CharField(max_length=500)
    size = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    def __str__(self):
        return self.name
class Profile(models.Model):
    """
    This model extends the built-in User model using a OneToOne relationship.
    """
    # Set up the one-to-one relationship with the User model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    verified = models.BooleanField(default=False)
    # If you want to allow a Text or CharField to be empty, use this pairing
    #   of default="" and blank=True instead of null=True.
    #   c.f.: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.Field.null
    title = models.TextField(default="", blank=True)
    location = models.CharField(max_length=100, default="", blank=True)
