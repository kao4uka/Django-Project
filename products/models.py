from django.db import models


class Hashtag(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    create_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=355)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="reviews")
    create_date =models.DateField(auto_now_add=True)


