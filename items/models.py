from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


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
    image = models.ImageField(null=True, blank=True)
    rating_total = models.DecimalField(max_digits=4, decimal_places=2, blank=False, null=False, default=0)

    def __str__(self):
        return self.name

    def adjust_rating_total(self):
        self.one_star_total = self.item_rating.aggregate(Avg('one_star'))['one_star__avg'] or 0
        self.two_stars_total = self.item_rating.aggregate(Avg('two_stars'))['two_stars__avg'] or 0
        self.three_stars_total = self.item_rating.aggregate(Avg('three_stars'))['three_stars__avg'] or 0
        self.four_stars_total = self.item_rating.aggregate(Avg('four_stars'))['four_stars__avg'] or 0
        self.five_stars_total = self.item_rating.aggregate(Avg('five_stars'))['five_stars__avg'] or 0
        self.rating_total = self.one_star_total + self.two_stars_total + self.three_stars_total + self.four_stars_total + self.five_stars_total
        self.save()

class Rating(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_user')
    one_star = models.IntegerField(blank=True, null=True)
    two_stars = models.IntegerField(blank=True, null=True)
    three_stars = models.IntegerField(blank=True, null=True)
    four_stars = models.IntegerField(blank=True, null=True)
    five_stars = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item.name 

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_user')
    review_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.body