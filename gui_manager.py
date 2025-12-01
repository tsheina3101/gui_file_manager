import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import datetime
import commands
from commands import copy_file, delete_file, find_folder, count_files, add_date

#import commands

# Создание основного окна
root = tk.Tk()
root.title("Файловый менеджер")
root.geometry("600x600")
root.resizable(width=False, height=False)
root.configure(background="white")

# Создание заголовка
header = tk.Label(root, text="Файловый менеджер", font=("Cambria", 20, "bold"), bg="white", fg="black")
header.pack()
help = tk.Label(root, text = "Для выполнения действия нажмите соответствующую кнопку", font=("Arial", 10), bg="white", fg="black")
help.pack()

# Создание кнопок
copy_image = tk.PhotoImage(file="copy.png")
copy_button = tk.Button(image=copy_image, width=64, height=64, command=copy_file)
delete_image = tk.PhotoImage(file="delete.png")
delete_button = tk.Button(root, image=delete_image, width=64, height=64, command=delete_file)
find_image = tk.PhotoImage(file="search.png")
find_button = tk.Button(root, image=find_image, width=64, height=64, command=find_folder)
count_image = tk.PhotoImage(file="count.png")
count_button = tk.Button(root, image=count_image, width=64, height=64, command=count_files)
date_image = tk.PhotoImage(file="date.png")
date_button = tk.Button(root, image=date_image, width=64, height=64, command=add_date)

# Размещение кнопок в окне
copy_button.place(x=20, y=100)
delete_button.place(x=20, y=200)
find_button.place(x=20, y=300)
count_button.place(x=20, y=400)
date_button.place(x=20, y=500)

# Создание меток
copy_label = tk.Label(root, text="Копирование файла", bg="white", fg="black", font=("Arial", 15))
delete_label = tk.Label(root, text="Удаление файлов и папок", bg="white", fg="black", font=("Arial", 15))
find_label = tk.Label(root, text="Поиск папки", bg="white", fg="black", font=("Arial", 15))
count_label = tk.Label(root, text="Подсчет количества файлов в папке", bg="white", fg="black", font=("Arial", 15))
date_label = tk.Label(root, text="Добавление даты к имени файла", bg="white", fg="black", font=("Arial", 15))

# Размещение меток в окне
copy_label.place(x=100, y=115)
delete_label.place(x=100, y=215)
find_label.place(x=100, y=315)
count_label.place(x=100, y=415)
date_label.place(x=100, y=515)

# Запуск основного цикла обработки событий
root.mainloop()