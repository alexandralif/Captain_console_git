from django.db import models


class product_category(models.Model):
    name = models.CharField(max_length=255)


class products(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(product_category, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()

    def __str__(self):
        return self.name


class product_image(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(products, on_delete=models.CASCADE)

    def __str__(self):
        return self.image
