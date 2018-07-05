"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Input (models.Model):
    Value1 = models.FloatField(default=0.0)
    Value2 = models.FloatField(default=0.0)
    Value3 = models.FloatField(default=0.0)
    Value4 = models.FloatField(default=0.0)
    Value5 = models.FloatField(default=0.0)
    Value6 = models.FloatField(default=0.0)
    Value7 = models.FloatField(default=0.0)
    Value8 = models.FloatField(default=0.0)

    def __str__(self):
        return self.Parameter


class Output (models.Model):
    #id = models.FloatField(default=0.0, primary_key=True)
    Value1 = models.FloatField()
    Value2 = models.FloatField(default=0.0)
    Value3 = models.FloatField(default=0.0)
    Value4 = models.FloatField(default=0.0)
    Value5 = models.FloatField(default=0.0)
    Value6 = models.FloatField(default=0.0)
    Value7 = models.FloatField(default=0.0)
    Value8 = models.FloatField(default=0.0)

    def __str__(self):
        return self.Parameter


class UserProfile (models.Model):
    User = models.OneToOneField(User)
    Institution = models.CharField(max_length=100, default='')
    Description = models.CharField(max_length=100, default='')
    Website = models.URLField(default='')
    Contact = models.CharField(max_length=100, default='')