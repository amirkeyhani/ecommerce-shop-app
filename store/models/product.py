from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/products/', null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(default=0, decimal_places=3, max_digits=9)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()