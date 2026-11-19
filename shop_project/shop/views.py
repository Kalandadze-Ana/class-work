from django.shortcuts import render
from .models import Product, Customer

def home(request):
    products_exact = Product.objects.filter(name__exact="Laptop")
    customers_contains = Customer.objects.filter(last_name__contains="Ber")
    products_startswith = Product.objects.filter(name__startswith="Sam")
    products_endswith = Product.objects.filter(name__endswith="Pro")



    products_gt = Product.objects.filter(price__gt=100)
    products_gte = Product.objects.filter(price__gte=100)
    products_lt = Product.objects.filter(price__lt=100)
    products_lte = Product.objects.filter(price__lte=100)
    products_range = Product.objects.filter(price__range=(10, 50))


    products_in = Product.objects.filter(id__in=[1, 2])
    customers_isnull = Customer.objects.filter(email__isnull=True)

    context = {
        'products_exact': products_exact,
        'customers_contains': customers_contains,
        'products_startswith': products_startswith,
        'products_endswith': products_endswith,
        'products_gt': products_gt,
        'products_gte': products_gte,
        'products_lt': products_lt,
        'products_lte': products_lte,
        'products_range': products_range,
        'products_in': products_in,
        'customers_isnull': customers_isnull,
    }


    return render(request, 'home.html', context)



