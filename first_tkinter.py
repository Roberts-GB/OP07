import tkinter as tk

def my_summa():
    numbers = entry.get().split()
    result = sum(int(number) for number in numbers)
    label.config(text=f"Сумма чисел - {result}")

root = tk.Tk()
root.title("Сумма чисел")
label = tk.Label(root, text="Введите числа через пробел")
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Посчитать сумму", command=my_summa)
button.pack()
root.mainloop()
