import csv
import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Имя файла с данными
CSV_FILE = "users.csv"


def load_data_from_csv():
    """Функция загрузки данных из CSV-файла."""
    if not os.path.exists(CSV_FILE):
        create_test_csv()

    data = []
    try:
        with open(CSV_FILE, mode="r", encoding="utf-8-sig") as f:
            reader = csv.reader(f, delimiter=";")
            next(reader)  # Пропускаем заголовок

            for row in reader:
                if row:  # Проверка на пустые строки
                    data.append(row)
    except Exception as e:
        messagebox.showerror(
            "Ошибка", f"Не удалось прочитать файл {CSV_FILE}:\n{e}"
        )
    return data


def create_test_csv():
    """Создает тестовый файл, если его не существует."""
    test_data = [
        ["id", "name", "email", "role"],
        ["1", "Алексей", "artyombirulya@gmail.com", "Админ"],  # Ваш email для теста
        ["2", "Мария", "maria@example.com", "Пользователь"],
        ["3", "Иван", "ivan@example.com", "Модератор"],
    ]
    with open(CSV_FILE, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(test_data)


def send_emails():
    """Функция рассылки писем по всему списку из таблицы."""
    all_items = tree.get_children()

    if not all_items:
        messagebox.showwarning("Внимание", "Список пользователей пуст!")
        return

    sent_count = 0

    # Проходим циклом по каждой строке таблицы
    for item in all_items:
        values = tree.item(item, "values")
        user_name = values[1]
        user_email = values[2]

        print(f"Отправка на {user_email}: Hello, {user_name}!")

        # НАСТРОЙКИ ЯНДЕКСА
        SENDER = "artmbirulya@yandex.com"  # Изменили .com на .ru
        PASSWORD = "fiwvbwzisbfnincq"  # Ваш 16-значный пароль приложения
        RECIPIENT = user_email

        # Создание письма
        msg = EmailMessage()
        msg["Subject"] = "Тестовое письмо"
        msg["From"] = SENDER
        msg["To"] = RECIPIENT
        msg.set_content(
            f"Hello, {user_name}!\n\nУра! Код на Python работает, и письмо успешно отправлено!"
        )

        # Отправка через сервер Яндекса
        try:
            with smtplib.SMTP_SSL("smtp.yandex.ru", 465) as server:
                server.set_debuglevel(1)  # Логи включаются ДО авторизации
                server.login(SENDER, PASSWORD)
                server.send_message(msg)

            print(f"Письмо для {user_name} успешно отправлено!")
            sent_count += 1  # Считаем только успешные

        except Exception as e:
            print(f"Произошла ошибка при отправке на {user_email}: {e}")
            messagebox.showerror(
                "Произошла ошибка при отправке",
                f"Не удалось отправить письмо для {user_name} ({user_email}):\n{e}",
            )

    # ОКНО УВЕДОМЛЕНИЯ (Вынесено из цикла наружу)
    if sent_count > 0:
        messagebox.showinfo(
            "Рассылка завершена",
            f"Успешно отправлено писем: {sent_count}.",
        )


# --- ИНТЕРФЕЙС TKINTER ---

root = tk.Tk()
root.title("Панель рассылки пользователям")
root.geometry("550x350")

# Создаем контейнер для таблицы и скроллбара
container = ttk.Frame(root)
container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Создаем вертикальный скроллбар
scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Создаем таблицу (Treeview)
columns = ("id", "name", "email", "role")
tree = ttk.Treeview(
    container, columns=columns, show="headings", yscrollcommand=scrollbar.set
)
scrollbar.config(command=tree.yview)

# Задаем заголовки колонок
tree.heading("id", text="ID")
tree.heading("name", text="Имя")
tree.heading("email", text="Email")
tree.heading("role", text="Роль")

# Задаем размеры колонок
tree.column("id", width=40, anchor=tk.CENTER)
tree.column("name", width=120)
tree.column("email", width=180)
tree.column("role", width=100)

# Загружаем данные из файла и вставляем в таблицу
users_data = load_data_from_csv()
for user in users_data:
    tree.insert("", tk.END, values=user)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# КНОПКА РАССЫЛКИ (Снизу)
btn_send = ttk.Button(
    root, text="Разослать 'hello' всем пользователям", command=send_emails
)
btn_send.pack(pady=15, ipady=5, fill=tk.X, padx=10)

root.mainloop()
