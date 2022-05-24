from django.db import models
from django.urls import reverse


# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=30)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)


    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=35)
    price = models.FloatField(default=0)
    product_date = models.DateTimeField()
    update_date = models.DateTimeField(auto_now=True)
    brands = models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=True)
    image = models.ImageField(upload_to = 'mobile_images')

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-id']


    # def get_absolute_url(self):
    #     return reverse("product:product-details", kwargs={"id": self.id})


class User(models.Model):
    pass