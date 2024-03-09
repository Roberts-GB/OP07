import tkinter as tk
from math import sqrt, pow

# Функции для операций калькулятора
def calculate():
    try:
        # Замените символы для выполнения операций
        result = eval(entry.get().replace('x', '*').replace('÷', '/'))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def add_to_entry(text):
    current_text = entry.get()
    if current_text == '0':
        entry.delete(0, tk.END)
    entry.insert(tk.END, text)

def clear_entry():
    entry.delete(0, tk.END)
    entry.insert(0, '0')

def square():
    try:
        current_value = float(entry.get())
        squared_value = pow(current_value, 2)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(squared_value))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def square_root():
    try:
        current_value = float(entry.get())
        if current_value >= 0:
            sqrt_value = sqrt(current_value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(sqrt_value))
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

def change_sign():
    try:
        current_value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(-current_value))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

# Словарь соответствия текста кнопок и функций
operations = {
    'C': clear_entry,
    '=': calculate,
    'x²': square,
    '√': square_root,
    '+/-': change_sign,
}

# Обработчик нажатия кнопки
def on_click(text):
    if text in operations:
        operations[text]()
    else:
        add_to_entry(text)

root = tk.Tk()
root.title("Калькулятор")

# Поле ввода
entry = tk.Entry(root, justify='right', font=('Arial', 20, 'bold'))
entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
entry.insert(0, '0')

# Определение цветов кнопок
button_colors = {
    'C': 'red',
    '=': 'orange',
    'op': 'lightgreen',
    'num': 'lightgrey'
}

# Создание кнопок
buttons = [
    ('√', 1, 0, 'op'), ('x²', 1, 1, 'op'), ('+/-', 1, 2, 'op'), ('C', 1, 3, 'C'),
    ('7', 2, 0, 'num'), ('8', 2, 1, 'num'), ('9', 2, 2, 'num'), ('÷', 2, 3, 'op'),
    ('4', 3, 0, 'num'), ('5', 3, 1, 'num'), ('6', 3, 2, 'num'), ('x', 3, 3, 'op'),
    ('1', 4, 0, 'num'), ('2', 4, 1, 'num'), ('3', 4, 2, 'num'), ('-', 4, 3, 'op'),
    ('0', 5, 0, 'num'), ('.', 5, 1, 'num'), ('=', 5, 2, '='), ('+', 5, 3, 'op'),
]

# Расположение кнопок на сетке
for (text, row, column, color_key) in buttons:
    color = button_colors[color_key]
    btn = tk.Button(root, text=text, bg=color, font=('Arial', 20, 'bold'), command=lambda t=text: on_click(t))
    btn.grid(row=row, column=column, sticky='nsew', padx=1, pady=1)

# Настройка расширения кнопокпри изменении размера окна
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
