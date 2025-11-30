import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import datetime
#import commands


# Создание основного окна
root = tk.Tk()
root.title("Файловый менеджер")
root.geometry("600x600")
root.resizable(width=False, height=False)
root.configure(background="white")

# Создание заголовка
header = tk.Label(root, text="Файловый менеджер", font=("Arial", 20, "bold"), bg="white", fg="blue")
header.pack()

# Создание кнопок
copy_image = tk.PhotoImage(file = "copy.png")
copy_button = tk.Button(root, image = copy_image, width = 64, height = 64)
delete_image = tk.PhotoImage(file = "delete.png")
delete_button = tk.Button(root, image = delete_image, width = 64, height = 64)
find_image = tk.PhotoImage(file = "search.png")
find_button = tk.Button(root, image = find_image, width = 64, height = 64)
count_image = tk.PhotoImage(file = "count.png")
count_button = tk.Button(root, image = count_image, width = 64, height = 64)
date_image = tk.PhotoImage(file = "date.png")
date_button = tk.Button(root, image = date_image, width = 64, height = 64)

# Размещение кнопок в окне
copy_button.pack(pady=5)
delete_button.pack(pady=5)
find_button.pack(pady=5)
count_button.pack(pady=5)
date_button.pack(pady=5)


# Запуск основного цикла обработки событий
root.mainloop()