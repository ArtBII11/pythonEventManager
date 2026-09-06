import os
import tkinter as tk
from tkinter import filedialog, messagebox

# 1. Создаем глобальную переменную. Сюда запишется текст из файла.
mail_body = ""


def attach_file():
    global mail_body  # Обязательно пишем global, чтобы изменить переменную внутри функции
    file_formats = [("Текстовые файлы (*.txt)", "*.txt")]

    full_path = filedialog.askopenfilename(
        title="Выберите файл с текстом письма", filetypes=file_formats
    )

    if full_path:
        file_name = os.path.basename(full_path)
        try:
            with open(full_path, "r", encoding="utf-8") as file:
                # Читаем текст и сохраняем в нашу глобальную переменную
                mail_body = file.read()

            # Также выводим этот текст в окошко, чтобы пользователь его видел
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", mail_body)

            label_status.config(text=f"Файл '{file_name}' загружен", fg="green")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось прочитать файл:\n{e}")


# 2. Функция, которая отправляет письмо
def send_email():
    # САМЫЙ НАДЕЖНЫЙ СПОСОБ: берем текст напрямую из текстового поля экрана,
    # чтобы точно подхватить все абзацы и изменения, которые сделал пользователь
    text_from_screen = text_area.get("1.0", tk.END).strip()

    if not text_from_screen:
        messagebox.showwarning("Внимание", "Письмо пустое! Нечего отправлять.")
        return

    # Теперь в переменной text_from_screen лежит ваш готовый текст с абзацами.
    # Передаем её в ваш код отправки письма:
    print("--- НАЧАЛО ПИСЬМА ---")
    print(text_from_screen)  # Вы увидите в консоли, что текст перенесся с абзацами
    print("--- КОНЕЦ ПИСЬМА ---")

    # Имитация отправки (сюда вставьте ваш код, например, для smtplib или requests)
    messagebox.showinfo(
        "Успех", "Текст успешно перенесен в письмо и готов к отправке!"
    )


# Создаем интерфейс
root = tk.Tk()
root.title("Подготовка письма")
root.geometry("500x450")

# Кнопка прикрепления
btn_attach = tk.Button(root, text="📎 Прикрепить текст из файла", command=attach_file)
btn_attach.pack(pady=10)

label_status = tk.Label(root, text="Файл не выбран", fg="gray")
label_status.pack()

# Текстовое поле (обязательно wrap="word" для красивых абзацев)
text_area = tk.Text(root, wrap="word", height=12, width=55)
text_area.pack(pady=10)

# Кнопка отправки
btn_send = tk.Button(
    root, text="✉️ Отправить это письмо", bg="#4CAF50", fg="white", command=send_email
)
btn_send.pack(pady=10)

root.mainloop()
