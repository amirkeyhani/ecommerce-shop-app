from django.db import models
from .product import Product
from .customer import Customer

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=3, max_digits=9)
    quantity = models.IntegerField(default=0)
    ordered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    status = models.BooleanField(default=False)
    
    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('ordered_at')