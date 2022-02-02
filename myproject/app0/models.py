import string
from django.db import models

# Create your models here.
# class Feature:
#     id: int
#     name: str
#     details: str
#     is_true: bool

# each class is assigned an ID, so no need to define a field called id,
# the param models.Model converts this class to a Django model
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    

