from django.db import models

class product_category(models.Model):
    '''this is our product category model. We use that so we can sort the products by a manufacturer e.g.'''
    name = models.CharField(max_length=255)


class product_type(models.Model):
    '''this is the product type model class. We use that so that we can display of what type each product is'''
    name = models.CharField(max_length=255)


class products(models.Model):
    '''this is our model for all the products that the website sells'''
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(product_category, on_delete=models.CASCADE)
    price = models.IntegerField()
    on_sale = models.BooleanField()
    type = models.ForeignKey(product_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class product_image(models.Model):
    '''this is the image model for images connected to a product'''
    image = models.CharField(max_length=999)
    product = models.ForeignKey(products, on_delete=models.CASCADE) #this foreign key connects the images to the products model

    def __str__(self):
        return self.image

