import tkinter as tk

root = tk.Tk()
root.geometry("400x220")
root.title("Вызов функции из функции")

# 1. ВТОРАЯ ФУНКЦИЯ: Чистая математика
# Она ничего не знает про Tkinter, а просто берет два числа и вычитает их
def math_subtraction(value_a, value_b):
    return value_a - value_b


# 2. ПЕРВАЯ ФУНКЦИЯ: Сбор данных из интерфейса
def handle_input_change(*args):
    # Достаем текст из переменных инпутов
    num1_text = num1_var.get()
    num2_text = num2_var.get()
    
    # Безопасно переводим в цифры
    try:
        digit1 = float(num1_text) if num1_text else 0.0
    except ValueError:
        digit1 = 0.0
        
    try:
        digit2 = float(num2_text) if num2_text else 0.0
    except ValueError:
        digit2 = 0.0

    # ВЫЗЫВАЕМ ВТОРУЮ ФУНКЦИЮ и передаем ей наши цифры
    final_result = math_subtraction(digit1, digit2)
    
    # Отображаем результат выполнения второй функции на экране
    result_label.config(text=f"Результат вычитания: {final_result:.2f}")


# Настройка переменных и интерфейса
num1_var = tk.StringVar(value="0")
num2_var = tk.StringVar(value="0")

# Включаем отслеживание изменений
num1_var.trace_add("write", handle_input_change)
num2_var.trace_add("write", handle_input_change)

# Виджеты ввода
tk.Label(root, text="Число А:").pack(pady=(10, 0))
tk.Entry(root, textvariable=num1_var, font=("Arial", 12)).pack()

tk.Label(root, text="Число Б (вычитается из А):").pack(pady=(10, 0))
tk.Entry(root, textvariable=num2_var, font=("Arial", 12)).pack()

# Надпись для вывода результата
result_label = tk.Label(root, text="Результат вычитания: 0.00", font=("Arial", 14, "bold"), fg="darkgreen")
result_label.pack(pady=20)

root.mainloop()
