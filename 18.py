import os

def is_file_empty(file_name):
    return os.path.getsize(file_name) == 0

if is_file_empty("data.txt"):
    print("Файл data.txt є порожнім")
else:
    print("Файл data.txt не є порожнім")