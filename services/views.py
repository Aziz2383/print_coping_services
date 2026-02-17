from django.shortcuts import render
from .models import Service


def service_list(request):
    items = Service.objects.filter(is_active=True).select_related("category")
    return render(request, "services/list.html", {"items": items})
