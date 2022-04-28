"""
Definition of models.
"""

from django.db import models
from enum import Enum

class Category(Enum):
    Coffee = "Coffee"
    Tea = "Tea"
    Smoothie = "Smoothie"
    Juice = "Juice"

class Size(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"

class Drink(models.Model):
    category = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.name) for tag in Category],
        default=''
        )
    size = models.CharField(
        max_length=10,
        choices=[(tag.value, tag.name) for tag in Size]
        )
    quantity = models.IntegerField(default=1)

    @property
    def price(self):
        x = 0
        if(self.category == "Coffee"):
            x += 10
        if(self.category == "Juice"):
            x += 15
        if(self.category == "Smoothie"):
            x += 20
        if(self.category == "Tea"):
            x += 5
        if(self.size == "Medium"):
            x += 5
        if(self.size == "Large"):
            x += 10
        
        return self.quantity * x

    order_date = models.DateTimeField(auto_now=True)



