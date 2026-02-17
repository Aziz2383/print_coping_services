import requests
from django.conf import settings


def send_telegram_message(text: str) -> None:
    token = getattr(settings, "TELEGRAM_BOT_TOKEN", "")
    chat_id = getattr(settings, "TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "disable_web_page_preview": True,
    }
    requests.post(url, data=payload, timeout=10)


def send_telegram_document(caption: str, file_field) -> None:
    """
    file_field: например order.file (FileField)
    """
    token = getattr(settings, "TELEGRAM_BOT_TOKEN", "")
    chat_id = getattr(settings, "TELEGRAM_CHAT_ID", "")
    if not token or not chat_id or not file_field:
        return

    url = f"https://api.telegram.org/bot{token}/sendDocument"

    # file_field.file — это файловый объект Django
    file_field.open("rb")
    try:
        files = {
            "document": (file_field.name.split("/")[-1], file_field.file),
        }
        data = {
            "chat_id": chat_id,
            "caption": caption,
        }
        requests.post(url, data=data, files=files, timeout=30)
    finally:
        file_field.close()
