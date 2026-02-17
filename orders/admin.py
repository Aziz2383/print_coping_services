from django.contrib import admin
from django.conf import settings
from .models import Order
from .telegram import send_telegram_message


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("created_at", "name", "phone", "service", "status")
    list_filter = ("status", "created_at")
    search_fields = ("name", "phone")
    list_editable = ("status",)

    def save_model(self, request, obj, form, change):
        # Проверяем — статус изменился?
        if change:
            old_obj = Order.objects.get(pk=obj.pk)
            if old_obj.status != obj.status:
                if obj.status == Order.STATUS_DONE:
                    text = (
                        f"✅ Заявка #{obj.id} готова\n"
                        f"👤 Имя: {obj.name}\n"
                        f"📞 Телефон: {obj.phone}"
                    )
                    send_telegram_message(text)

        super().save_model(request, obj, form, change)
