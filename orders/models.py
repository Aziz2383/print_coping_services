from django.db import models
from services.models import Service

class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField("Имя", max_length=120)
    phone = models.CharField("Телефон", max_length=50)
    comment = models.TextField("Комментарий", blank=True)

    file = models.FileField("Макет (файл)", upload_to="order_files/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_NEW = "new"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_DONE = "done"

    STATUS_CHOICES = [
        (STATUS_NEW, "Новая"),
        (STATUS_IN_PROGRESS, "В работе"),
        (STATUS_DONE, "Готово"),
    ]

    status = models.CharField(
        "Статус",
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
        db_index=True,
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.get_status_display()}"
