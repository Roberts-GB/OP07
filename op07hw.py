import tkinter as tk

# Функция, вызываемая при нажатии на кнопку
def say_hello():
    name = name_entry.get()  # Получаем имя из текстового поля
    greeting_label.config(text=f"Привет, {name}!")  # Обновляем текст метки с приветствием

# Создание основного окна
root = tk.Tk()
root.title("Приветствие")

# Создание метки с инструкцией
instruction_label = tk.Label(root, text="Введите ваше имя:")
instruction_label.pack()

# Создание текстового поля для ввода имени
name_entry = tk.Entry(root)
name_entry.pack()

# Создание кнопки, которая вызовет функцию say_hello при нажатии
greet_button = tk.Button(root, text="Поздороваться", command=say_hello)
greet_button.pack()

# Метка для вывода приветствия
greeting_label = tk.Label(root, text="")
greeting_label.pack()

# Запуск основного цикла обработки событий
root.mainloop()
