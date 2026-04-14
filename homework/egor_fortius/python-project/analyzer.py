import argparse
import os
import colorama
from colorama import Fore, Style


# Инициализация: autoreset=True автоматически сбрасывает цвет после каждого print()
colorama.init(autoreset=True)

# В программе обязательным аргументом будет путь к папке, в которой будет происходить поиск
parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Path to folder")
parser.add_argument("-t", "--text", required=True, help="Text for search in file")
parser.add_argument("-d", "--date", help="date for search (ex: YYYY-MM-DD)")
parser.add_argument("--time", help="Time for search (ex: hr:min)")
parser.add_argument("--full", help="full name.log", action="store_true")
args = parser.parse_args()

# print(args.folder, args.text, args.date, args.full)

# Проверяем, что папка существует
if not os.path.exists(args.folder):
    print("Folder not found")
    exit(1)

# получаем список всех файлов в папке
list_logs = os.listdir(args.folder)

# Открываем каждый файл и ищем в нем текст, если он есть, то выводим его на экран
for log in list_logs:
    if log.endswith(".log"):
        file_path = os.path.join(args.folder, log)
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    if args.text in line:
                        words = line.split()
                        if len(words) < 2:
                            continue
                        date_error = words[0]   # Дата ошибки
                        time_error = words[1][:5]   # Время ошибки
                        # Фильтрация по дате
                        if args.date and date_error != args.date:
                            continue
                        # Фильтрация по времени
                        if args.time and time_error != args.time:
                            continue
                        # Находим индекс текста в словах
                        try:
                            idx = words.index(args.text)
                        except ValueError:
                            continue
                        # Контекст: 5 слов до и после
                        context = " ".join(words[max(0, idx - 5):idx + 6])
                        highlighted_context = context.replace(
                            args.text, 
                            f"{Fore.RED}{Style.BRIGHT}{args.text}{Style.RESET_ALL}"
                        )
                        
                        filename = file_path if args.full else log
                        
                        # 🔹 Вывод с разными цветами для удобства чтения
                        print(f"{Fore.CYAN}{filename}{Fore.RESET} | "
                              f"{Fore.YELLOW}{date_error}{Fore.RESET} | "
                              f"{Fore.GREEN}{time_error}{Fore.RESET} | "
                              f"{highlighted_context}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
