import smtplib
import sys
from email.message import EmailMessage

# ================= НАСТРОЙКИ АВТОРИЗАЦИИ =================
# Укажите вашу ПОЛНУЮ почту Яндекс (проверьте каждую букву в логине!)
SENDER_EMAIL = "artmbirulya@yandex.com"  

# Вставьте 16-значный пароль приложения (БЕЗ пробелов)
APP_PASSWORD = "fiwvbwzisbfnincq"      

# Кому отправляем письмо
RECEIVER_EMAIL = "artmbirulya@yandex.com"
# =========================================================

def send_yandex_email():
    # 1. Создание структуры письма
    msg = EmailMessage()
    msg["Subject"] = "Тестовое письмо от Python"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    
    # Текст письма
    msg.set_content(
        "Привет!\n\n"
        "Это чистое тестовое письмо, отправленное через SMTP сервер Яндекса.\n"
        "Если вы видите этот текст, значит авторизация прошла успешно!"
    )

    print("Попытка подключения к smtp.yandex.ru...", flush=True)

    # 2. Подключение к серверу и отправка
    try:
        # Для Яндекса используется SSL и порт 465
        with smtplib.SMTP_SSL("smtp.yandex.ru", 465) as server:
            
            # Включаем максимальный уровень отладки (логи сервера пойдут прямо в консоль)
            server.set_debuglevel(1)
            
            print("\n=== НАЧАЛО SMTP ДИАЛОГА ===", flush=True)
            
            # Авторизация на сервере
            server.login(SENDER_EMAIL, APP_PASSWORD)
            
            # Отправка сообщения
            server.send_message(msg)
            
            print("=== КОНЕЦ SMTP ДИАЛОГА ===\n", flush=True)
            
        print("🎉 Успех! Письмо отправлено без ошибок.")
        
    except smtplib.SMTPAuthenticationError:
        print("\n❌ Ошибка 535: Ошибка авторизации!", file=sys.stderr)
        print("Проверьте: 1) Включен ли IMAP/SMTP в настройках почты Яндекса.", file=sys.stderr)
        print("2) Правильно ли написан логин. 3) Используется ли Пароль Приложения вместо обычного.", file=sys.stderr)
    except Exception as e:
        print(f"\n❌ Произошла непредвиденная ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    send_yandex_email()