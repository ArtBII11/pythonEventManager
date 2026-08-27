import sys
import csv
import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

CSV_FILE_MEET = "Meetings.csv"
CSV_FILE = "users.csv"

def load_data_from_csv():
    """Функция загрузки данных из CSV-файла."""
    if not os.path.exists(CSV_FILE):
        create_test_csv_users()

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


def create_test_csv_users():
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
        msg["Subject"] = f" meeting named{entry_name.get()}"
        print(entry_name.get())
        msg["From"] = SENDER
        msg["To"] = RECIPIENT
        msg.set_content(
            f"Hello, {user_name}!,our meeting data is {entry_data.get()} and time {entry_time.get()}."
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








placeholder_map = {}


def load_data_from_csv_meet():
    """Функция загрузки данных из CSV-файла."""
    # 1. Проверяем, существует ли файл
    if not os.path.exists(CSV_FILE_MEET):
        choice = messagebox.askyesno(
            "Не найден файл Meetings.csv", "Создать файл с шаблоном?"
        )
        if choice:
            create_test_csv_meet()  # Создаем файл
        else:
            root.destroy()
            sys.exit()

    data = []
    try:
        with open(CSV_FILE_MEET, mode="r", encoding="utf-8-sig") as f:
            reader = csv.reader(f, delimiter=";")
            next(reader)  # Пропускаем заголовок

            for row in reader:
                if row:  # Проверка на пустые строки
                    data.append(row)
    except Exception as e:
        messagebox.showerror(
            "Ошибка", f"Не удалось прочитать файл {CSV_FILE_MEET}:\n{e}"
        )

    return data
    


def create_test_csv_meet():
    #Создает тестовый файл, если его не существует.
    test_data = [
        ["name_of_meet", "end_date", "start_date"],
        ["Алексей", "02.04.26", "02.04.26"],  # Ваш email для теста
        ["Мария", "02.04.26", "02.04.26"],
        ["Иван", "02.04.26", "02.04.26"],
    ]
    with open(CSV_FILE_MEET, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(test_data)



def enter_function_input(event):
    text_placeholder = placeholder_map.get(event.widget)
    if event.widget.get() != text_placeholder and event.widget.get() != "":
        event.widget.config(state="readonly")



root = tk.Tk()
root.title("Event manager(Editing)")
root.geometry("750x750")


container = ttk.Frame(root)
container.grid(column=0,row=2,ipadx=30,ipady=30)


# Создаем таблицу (Treeview)
columns = ("id", "name", "email", "role")
tree = ttk.Treeview(
    container, columns=columns, show="headings"
)

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

tree.grid(column=0,row=2,ipadx=10,ipady=10)

# КНОПКА РАССЫЛКИ (Снизу)
btn_send = ttk.Button(
    root, text="Разослать 'hello' всем пользователям", command=send_emails
)
btn_send.grid(column=4,row=2,ipadx=10,ipady=10)


def off_entry_mouse(event):
    current_entry = event.widget
    text_placeholder = placeholder_map.get(current_entry)
    if current_entry.get() == "":
        current_entry.insert(0, text_placeholder)

def on_entry_click(event):
    current_entry = event.widget 
    text_placeholder = placeholder_map.get(current_entry)
    if current_entry.get() == text_placeholder:
        current_entry.delete(0, tk.END)


entry_name = ttk.Entry(root,font=("Arial", 13))
entry_name.grid(column=1,row=0,ipady=15,ipadx=100,pady=3)
placeholder_map[entry_name] = "Введите сюда название..."
entry_name.insert(0, "Введите сюда название...")


entry_name.bind("<FocusIn>", on_entry_click)
entry_name.bind("<FocusOut>",off_entry_mouse)
entry_name.bind("<Return>",enter_function_input)




entry_time = ttk.Entry(root)
entry_time.grid(column=0,row=1,pady=(80,5),ipady=5)
entry_time.insert(0,"Время...")
placeholder_map[entry_time] = "Время..."
entry_time.bind("<FocusIn>", on_entry_click)
entry_time.bind("<FocusOut>",off_entry_mouse)
entry_time.bind("<Return>",enter_function_input)


entry_data = ttk.Entry(root)
entry_data.grid(column=0,row=2,pady=(5,0),ipady=5)
entry_data.insert(0,"Дата...")
placeholder_map[entry_data] = "Дата..."
entry_data.bind("<FocusIn>", on_entry_click)
entry_data.bind("<FocusOut>",off_entry_mouse)
entry_data.bind("<Return>",enter_function_input)



# label_title = tk.Label(root, text="Список запланированных мероприятий",font=("Arial",12,"bold"))
# label_title.pack(pady=(20,0))

# container = ttk.Frame(root,height=200,width=600)#----Контейнер для схемы
# container.pack_propagate(False)
# container.pack(padx=20,pady=10)


# scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL)#----Скролбар
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# columns = ("name", "email", "role")
# tree = ttk.Treeview(
#     container, columns=columns, show="headings", yscrollcommand=scrollbar.set
# )
# scrollbar.config(command=tree.yview)

# # Задаем заголовки колонок

# tree.heading("name", text="Название мероприятия")
# tree.heading("email", text="Конец мероприятия")
# tree.heading("role", text="Начало мероприятия")

# # Задаем размеры колонок
# tree.column("name", width=120, anchor=tk.CENTER)
# tree.column("email", width=180)
# tree.column("role", width=100)

# users_data = load_data_from_csv()
# for user in users_data:
#     tree.insert("", tk.END, values=user)

# tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()