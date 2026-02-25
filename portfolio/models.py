from django.db import models

class PortfolioItem(models.Model):
    title = models.CharField("Название", max_length=200)
    image = models.ImageField("Фото", upload_to="portfolio/")
    description = models.CharField("Короткое описание", max_length=255, blank=True)

    is_active = models.BooleanField("Показывать", default=True)
    sort_order = models.PositiveIntegerField("Порядок", default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Портфолио"
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.title