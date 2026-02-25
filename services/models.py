from django.db import models
from slugify import slugify   # pip install python-slugify


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Визитки -> vizitki
        super().save(*args, **kwargs)

    def str(self):
        return self.title


class Service(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="services"
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price_from = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="services/", null=True, blank=True)

    def str(self):
        return self.title