from django.urls import path
from .views import service_list

app_name = "services"

urlpatterns = [
    path("", service_list, name="list"),
    path("category/<slug:category_slug>/", service_list, name="by_category"),
]