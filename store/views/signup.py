from django.shortcuts import render, redirect
from django.views import View

from store.models.customer import Customer
from django.contrib.auth.hashers import make_password

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        password = request.POST.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone_no': phone_no,
            'email': email,
            'password': password
        }
        error_message = None
        
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone_no=phone_no,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
    
    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = 'Please enter your First Name !!'
        elif len(customer.first_name) < 3:
            error_message = 'First name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please enter your Last Name !!'
        elif len(customer.last_name) < 3:
            error_message = 'Last Name must be 3 char long or more'
        elif not customer.phone_no:
            error_message = 'Enter your Phone Number'
        elif len(customer.phone_no) < 10:
            error_message = 'Phone number must be 10 char long'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long or more'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email address already registered..'
            
        return error_message