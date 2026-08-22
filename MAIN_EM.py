import csv
import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

CSV_FILE_MEET = "Meetings.csv"

def load_data_from_csv():
    """Функция загрузки данных из CSV-файла."""
    if not os.path.exists(CSV_FILE_MEET):
        create_test_csv()

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



def create_test_csv():
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

root = tk.Tk()
root.title("Event manager")
root.geometry("550x350")

label_title = tk.Label(root, text="Список запланированных мероприятий",font=("Arial",12,"bold"))
label_title.pack(pady=(20,0))

container = ttk.Frame(root,height=200,width=600)#----Контейнер для схемы
container.pack_propagate(False)
container.pack(padx=20,pady=10)


scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL)#----Скролбар
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

columns = ("name", "email", "role")
tree = ttk.Treeview(
    container, columns=columns, show="headings", yscrollcommand=scrollbar.set
)
scrollbar.config(command=tree.yview)

# Задаем заголовки колонок

tree.heading("name", text="Название мероприятия")
tree.heading("email", text="Конец мероприятия")
tree.heading("role", text="Начало мероприятия")

# Задаем размеры колонок
tree.column("name", width=120, anchor=tk.CENTER)
tree.column("email", width=180)
tree.column("role", width=100)

users_data = load_data_from_csv()
for user in users_data:
    tree.insert("", tk.END, values=user)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

def clicked():

    print("Ouh,braenz!")

btn = tk.Button(root, text = "Создать мероприятие" ,width=50,height=3,command=clicked)

btn.pack()


root.mainloop()