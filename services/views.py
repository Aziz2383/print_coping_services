from django.shortcuts import render, get_object_or_404
from .models import Service, Category

def service_list(request, category_slug=None):
    services = Service.objects.all().order_by("id")
    categories = Category.objects.all()

    current_category = None
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        services = services.filter(category=current_category)

    return render(request, "services/service_list.html", {
        "services": services,
        "categories": categories,
        "current_category": current_category,
    })