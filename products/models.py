from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)


