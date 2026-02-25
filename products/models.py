from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="products"
    )
    name = models.CharField("Название", max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    short_description = models.CharField("Краткое описание", max_length=255, blank=True)
    price_from = models.CharField("Цена от", max_length=80, blank=True)
    image = models.ImageField("Картинка", upload_to="product_images/", blank=True, null=True)

    is_active = models.BooleanField("Активно", default=True)
    sort_order = models.PositiveIntegerField("Порядок", default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name
