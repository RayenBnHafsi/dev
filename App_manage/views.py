from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.select_related().filter(featured=True)
    return render(
        request, 'base.html',
        {
            'products': products
        }
    )

def product(request,):
    return render(
        request, 'product.html'
    )


def slider(request,):
    products = Product.objects.select_related().filter(featured=True)
    return render(
        request, 'slider.html',
        {
            'products': products
        }
    )