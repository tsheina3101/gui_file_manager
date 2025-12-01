import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import datetime

def copy_file():
    """Копирует выбранный файл в указанную папку."""
    file_path = filedialog.askopenfilename(title="Выберите файл для копирования")
    if not file_path:
        return
    folder_path = filedialog.askdirectory(title="Выберите папку для копирования")
    if not folder_path:
        return
    try:
        shutil.copy2(file_path, folder_path)
        messagebox.showinfo("Успех", "Файл успешно скопирован!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось скопировать файл: {e}")

def delete_file():
    """Удаляет выбранный файл или папку."""
    path_to_delete = filedialog.askopenfilename(title="Выберите файл или папку для удаления")
    if not path_to_delete:
        path_to_delete = filedialog.askdirectory(title="Выберите файл или папку для удаления")
    if not path_to_delete:
        return
    try:
        if os.path.isfile(path_to_delete):
            os.remove(path_to_delete)
        else:
            shutil.rmtree(path_to_delete)
        messagebox.showinfo("Успех", "Файл/папка успешно удалены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось удалить файл/папку: {e}")

def find_folder():
    """Ищет папку внутри выбранной директории."""
    folder_name = tk.simpledialog.askstring("Поиск папки", "Введите имя папки для поиска:")
    if not folder_name:
        return
    search_path = filedialog.askdirectory(title="Выберите папку для поиска внутри")
    if not search_path:
        return

    for root, dirs, files in os.walk(search_path):
        if folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            messagebox.showinfo("Результат поиска", f"Папка найдена: {folder_path}")
            return

    messagebox.showerror("Ошибка", "Папка не найдена")

def count_files():
    """Подсчитывает количество файлов внутри выбранной папки (включая подпапки)."""
    folder_path = filedialog.askdirectory(title="Выберите папку для подсчета файлов")
    if not folder_path:
        return

    count = 0
    for root, dirs, files in os.walk(folder_path):
        count += len(files)

    messagebox.showinfo("Результат", f"Количество файлов: {count}")

def add_date():
    """Добавляет текущую дату к имени файла или ко всем файлам в папке."""
    file_or_folder = filedialog.askopenfilename(title="Выберите файл для переименования")
    if not file_or_folder:
        file_or_folder = filedialog.askdirectory(title="Выберите папку")
    if not file_or_folder:
        return
    date_str = datetime.date.today().strftime("%Y%m%d")

    if os.path.isfile(file_or_folder):
        name, ext = os.path.splitext(file_or_folder)
        new_name = f"{name}_{date_str}{ext}"
        os.rename(file_or_folder, new_name)
        messagebox.showinfo("Успех", f"Файл переименован в {new_name}")
    else:
        for filename in os.listdir(file_or_folder):
            filepath = os.path.join(file_or_folder, filename)
            if os.path.isfile(filepath):
                name, ext = os.path.splitext(filepath)
                new_name = f"{name}_{date_str}{ext}"
                new_path = os.path.join(file_or_folder, f"{os.path.basename(name)}_{date_str}{ext}")
                os.rename(filepath, new_path)
        messagebox.showinfo("Успех", "Имена файлов в папке обновлены")

