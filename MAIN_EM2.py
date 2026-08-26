import sys
import csv
import os
import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

CSV_FILE_MEET = "Meetings.csv"









placeholder_map = {}


# def load_data_from_csv():
#     """Функция загрузки данных из CSV-файла."""
#     # 1. Проверяем, существует ли файл
#     if not os.path.exists(CSV_FILE_MEET):
#         choice = messagebox.askyesno(
#             "Не найден файл Meetings.csv", "Создать файл с шаблоном?"
#         )
#         if choice:
#             create_test_csv()  # Создаем файл
#         else:
#             root.destroy()
#             sys.exit()

#     data = []
#     try:
#         with open(CSV_FILE_MEET, mode="r", encoding="utf-8-sig") as f:
#             reader = csv.reader(f, delimiter=";")
#             next(reader)  # Пропускаем заголовок

#             for row in reader:
#                 if row:  # Проверка на пустые строки
#                     data.append(row)
#     except Exception as e:
#         messagebox.showerror(
#             "Ошибка", f"Не удалось прочитать файл {CSV_FILE_MEET}:\n{e}"
#         )

#     return data
    


# def create_test_csv():
#     #Создает тестовый файл, если его не существует.
#     test_data = [
#         ["name_of_meet", "end_date", "start_date"],
#         ["Алексей", "02.04.26", "02.04.26"],  # Ваш email для теста
#         ["Мария", "02.04.26", "02.04.26"],
#         ["Иван", "02.04.26", "02.04.26"],
#     ]
#     with open(CSV_FILE_MEET, mode="w", encoding="utf-8-sig", newline="") as f:
#         writer = csv.writer(f, delimiter=";")
#         writer.writerows(test_data)

def enter_function_input(event):
    text_placeholder = placeholder_map.get(event.widget)
    if event.widget.get() == text_placeholder:
        root.focus_set()
        name_of_Meet = str(entry_name.get())
    return name_of_Meet


root = tk.Tk()
root.title("Event manager(Editing)")
root.geometry("550x750")



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
entry_name.bind("<Return>",enter_function_input)


entry_data = ttk.Entry(root)
entry_data.grid(column=0,row=2,pady=(5,0),ipady=5)
entry_data.insert(0,"Дата...")
placeholder_map[entry_data] = "Дата..."
entry_data.bind("<FocusIn>", on_entry_click)
entry_data.bind("<FocusOut>",off_entry_mouse)
entry_name.bind("<Return>",enter_function_input)

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