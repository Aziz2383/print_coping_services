from django.shortcuts import render
from .models import Product

def product_list(request):
    items = Product.objects.filter(is_active=True).select_related("category")
    return render(request, "products/list.html", {"items": items})
