import argparse
import os


# В программе обязательным аргументом будет путь к папке, в которой будет происходить поиск
parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Path to folder")
parser.add_argument("-t", "--text", required=True, help="Text for search in file")
parser.add_argument("-d", "--date", help="date for search")
parser.add_argument("--full", help="full name.log", action="store_true")
args = parser.parse_args()

# print(args.folder, args.text, args.date, args.full)

# Проверяем, что папка существует
if not os.path.exists(args.folder):
    print("Folder not found")
    exit(1)

# получаем список всех файлов в папке и выводим его на экран
list_logs = os.listdir(args.folder)
print(list_logs)