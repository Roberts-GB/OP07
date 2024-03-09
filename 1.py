import tkinter as tk
from math import sqrt, pow

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.create_entry()
        self.create_buttons()

    def create_entry(self):
        self.entry = tk.Entry(self.root, justify='right', font=('Arial', 20, 'bold'))
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')
        self.entry.insert(0, '0')

    def create_buttons(self):
        buttons = [
            ('√', 1, 0, 'op'), ('x²', 1, 1, 'op'), ('+/-', 1, 2, 'op'), ('C', 1, 3, 'C'),
            ('7', 2, 0, 'num'), ('8', 2, 1, 'num'), ('9', 2, 2, 'num'), ('÷', 2, 3, 'op'),
            ('4', 3, 0, 'num'), ('5', 3, 1, 'num'), ('6', 3, 2, 'num'), ('x', 3, 3, 'op'),
            ('1', 4, 0, 'num'), ('2', 4, 1, 'num'), ('3', 4, 2, 'num'), ('-', 4, 3, 'op'),
            ('0', 5, 0, 'num'), ('.', 5, 1, 'num'), ('=', 5, 2, '='), ('+', 5, 3, 'op'),
        ]
        button_colors = {'C': 'red', '=': 'orange', 'op': '#20B2AA', 'num': 'lightgrey'}
        for text, row, column, color_key in buttons:
            color = button_colors[color_key]
            btn = tk.Button(self.root, text=text, bg=color, font=('Arial', 20, 'bold'),
                            command=lambda t=text: self.on_click(t))
            btn.grid(row=row, column=column, sticky='nsew', padx=1, pady=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_click(self, text):
        if text == 'C':
            self.entry.delete(0, tk.END)
            self.entry.insert(0, '0')
        elif text == '=':
            self.calculate()
        elif text in ['√', 'x²', '+/-']:
            self.perform_operation(text)
        else:
            self.add_to_entry(text)

    def calculate(self):
        try:
            result = eval(self.entry.get().replace('x', '*').replace('÷', '/'))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Ошибка")

    def add_to_entry(self, text):
        current_text = self.entry.get()
        if current_text == '0':
            self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, text)

    def perform_operation(self, operation):
        try:
            current_value = float(self.entry.get())
            if operation == 'x²':
                result = pow(current_value, 2)
            elif operation == '√' and current_value >= 0:
                result = sqrt(current_value)
            elif operation == '+/-':
                result = -current_value
            else:
                raise ValueError
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except ValueError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Ошибка")

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
