from django.db import models

class Client(models.Model):
    name = models.CharField("Название", max_length=200)
    logo = models.ImageField("Логотип", upload_to="clients/")
    is_active = models.BooleanField("Показывать", default=True)
    sort_order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name