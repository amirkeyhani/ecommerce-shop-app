from django.shortcuts import render, redirect
from django.views import View
from store.models.customer import Customer
from store.models.order import Order
from store.models.product import Product

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone_no = request.POST.get('phone_no')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        
        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)),
                          address=address,
                          phone_no=phone_no)
            order.save()
            
        request.session['cart'] = {}
        
        return redirect('cart')