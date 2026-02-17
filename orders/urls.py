from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("order/", views.order_create, name="create"),
    path("thanks/", views.order_thanks, name="thanks"),
]
