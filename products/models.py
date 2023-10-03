from django.db import models


class Product(models.Model):
    """Model representing a product."""

    name = models.CharField(max_length=100)
    photo = models.URLField()
    category = models.CharField(max_length=50)
    offer_of_the_month = models.BooleanField()
    availability = models.BooleanField()
    self_pickup = models.BooleanField()
    description1 = models.TextField(max_length=500)
    description2 = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Product {self.name}"

    @property
    def description(self):
        """A property that combines two description fields"""

        return f"{self.description1} <br/> {self.description2}"
