from .models import Category

def services_categories(request):
    return {"nav_categories": Category.objects.all()}