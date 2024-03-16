from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    price = models.FloatField()
    discount = models.FloatField(blank=True, default=0)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    amount = models.IntegerField()
    vendor_code = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    product = models.ForeignKey(Product, related_name="characteristics", on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.key} - {self.value}"
