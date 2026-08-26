import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("550x250")

# 1. СОЗДАЕМ КАРТУ ПОДСКАЗОК (Словарь)
# Мы свяжем системные имена полей ввода с их текстами-подсказками
placeholder_map = {}


def clear_placeholder(event):
    """Общая функция очистки (работает, как мы разбирали ранее)."""
    current_entry = event.widget
    # Берем подсказку, которая закреплена за этим конкретным инпутом
    text_placeholder = placeholder_map.get(current_entry)

    if current_entry.get() == text_placeholder:
        current_entry.delete(0, tk.END)


# 2. ОБЩАЯ ФУНКЦИЯ ВОЗВРАТА ПОДСКАЗКИ
def restore_placeholder(event):
    # event.widget сообщает, из какого поля ушел курсор
    current_entry = event.widget

    # Ищем в нашем словаре, какая подсказка должна быть у этого инпута
    text_placeholder = placeholder_map.get(current_entry)

    # Главное условие: если пользователь ничего не написал (поле абсолютно пустое)
    if current_entry.get() == "":
        # Возвращаем на место именно его родную подсказку
        current_entry.insert(0, text_placeholder)


# --- СОЗДАНИЕ И НАСТРОЙКА ПОЛЕЙ ---

# ПОЛЕ 1: Название
entry_name = ttk.Entry(root, font=("Arial", 16))
entry_name.grid(column=1, row=0, rowspan=2, padx=8, pady=15, ipady=15, sticky="ew")
entry_name.insert(0, "Введите сюда название...")
# Запоминаем: для entry_name подсказка — "Введите сюда название..."
placeholder_map[entry_name] = "Введите сюда название..."

# ПОЛЕ 2: Время
entry_time = ttk.Entry(root)
entry_time.grid(column=0, row=0, padx=8, pady=15, ipady=5, sticky="ew")
entry_time.insert(0, "Время...")
# Запоминаем: для entry_time подсказка — "Время..."
placeholder_map[entry_time] = "Время..."

# ПОЛЕ 3: Дата
entry_data = ttk.Entry(root)
entry_data.grid(column=0, row=1, padx=8, pady=15, ipady=5, sticky="ew")
entry_data.insert(0, "Дата...")
# Запоминаем: для entry_data подсказка — "Дата..."
placeholder_map[entry_data] = "Дата..."


# 3. АВТОМАТИЧЕСКАЯ ПОМЕТКА ВСЕХ ПОЛЕЙ СРАЗУ
# Говорим Tkinter: "Пусть ВСЕ элементы ttk.Entry реагируют на вход и выход курсора"
root.bind_class("TEntry", "<FocusIn>", clear_placeholder)
root.bind_class("TEntry", "<FocusOut>", restore_placeholder)

root.mainloop()