from django.shortcuts import render, redirect
from django.conf import settings
from .forms import OrderForm
from .telegram import send_telegram_message, send_telegram_document


def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save()

            comment = (order.comment or "").strip()
            admin_link = f"{settings.SITE_URL}/admin/orders/order/{order.id}/change/"

            text = (
                "🆕 Новая заявка\n"
                f"🛠 Услуга: {order.service or '—'}\n"
                f"👤 Имя: {order.name}\n"
                f"📞 Телефон: {order.phone}\n"
            )
            if comment:
                text += f"💬 Комментарий: {comment}\n"
            text += f"🔗 Админка: {admin_link}"

            # 1) всегда отправим текст
            send_telegram_message(text)

            # 2) если есть файл — отправим файлом
            if order.file:
                caption = f"📎 Макет для заявки #{order.id} ({order.service or '—'})"
                send_telegram_document(caption, order.file)

            return redirect("orders:thanks")
    else:
        form = OrderForm()

    return render(request, "orders/order_form.html", {"form": form})


def order_thanks(request):
    return render(request, "orders/thanks.html")
