from unittest.util import _MAX_LENGTH
from django.db import models

class ItemChocolateList(models.Model):
    item_name = models.CharField(max_length=50)
    item_articleNumber = models.IntegerField()
    item_flavour = models.TextField()
    item_price = models.FloatField()
    item_tan = models.CharField(max_length=5)


