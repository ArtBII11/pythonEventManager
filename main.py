import csv
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# Изменяю для прверки GIT
# Имя файла с данными
CSV_FILE = "users.csv"


def load_data_from_csv():
    """Функция загрузки данных из CSV-файла."""
    # Если файла еще нет, создадим тестовый для примера
    if not os.path.exists(CSV_FILE):
        create_test_csv()

    data = []
    try:
        # Открываем файл с кодировкой utf-8-sig (убирает невидимый маркер Excel BOM)
        with open(CSV_FILE, mode="r", encoding="utf-8-sig") as f:
            # Excel в СНГ использует точку с запятой в качестве разделителя CSV
            reader = csv.reader(f, delimiter=";")
            header = next(reader)  # Пропускаем строку-заголовок (id;name...)

            for row in reader:
                if row:  # Проверка на пустые строки
                    data.append(row)
    except Exception as e:
        messagebox.showerror(
            "Ошибка", f"Не удалось прочитать файл {CSV_FILE}:\n{e}"
        )

    return data


def create_test_csv():
    """Создает файл, если его не существует."""
    test_data = [
        ["id", "name", "email", "role"],
        ["1", "Алексей", "alex@example.com", "Админ"],
        ["2", "Мария", "maria@example.com", "Пользователь"],
        ["3", "Иван", "ivan@example.com", "Модератор"],
    ]
    with open(CSV_FILE, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(test_data)


def send_emails():
    """Функция рассылки писем по всему списку из таблицы."""
    # Получаем все строки, которые сейчас отображаются в Grid (Treeview)
    all_items = tree.get_children()

    if not all_items:
        messagebox.showwarning("Внимание", "Список пользователей пуст!")
        return

    sent_count = 0

    # Проходим циклом по каждой строке таблицы
    for item in all_items:
        # Извлекаем значения колонок (возвращает кортеж: id, name, email, role)
        values = tree.item(item, "values")
        user_name = values[1]
        user_email = values[2]

        # Логика отправки
        print(f"Отправка на {user_email}: Hello, {user_name}!")
        # Здесь в будущем будет реальный код SMTP. Пока имитируем отправку.

        sent_count += 1

    # Показываем красивое окно об успешном завершении
    messagebox.showinfo(
        "Рассылка завершена",
        f"Успешно обработано пользователей: {sent_count}.\nВсем отправлено сообщение 'hello'!",
    )


# --- ИНТЕРФЕЙС ТКINTER ---

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
# Размещаем кнопку с отступами снизу таблицы
btn_send.pack(pady=15, ipady=5, fill=tk.X, padx=10)

root.mainloop()
