from django.db import models
from django.contrib.auth.models import User


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
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_user')
    one_star = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.item.name

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    review_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.body