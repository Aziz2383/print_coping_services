from clients.models import Client
from django.shortcuts import render
from portfolio.models import PortfolioItem


def home(request):
    works = PortfolioItem.objects.filter(is_active=True)[:8]
    clietns = Client.objects.filter(is_active=True)[:24]
    return render(request, "core/home.html", {
        "works": works,
        "clients": clietns,
    })

def contacts(request):
    return render(request, "core/contacts.html")