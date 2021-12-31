from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    display_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.display_name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=250)
    bio = models.TextField()
    sku = models.CharField(max_length=250, blank=True, null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    reviews = models.DecimalField(decimal_places=1, max_digits=3)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name