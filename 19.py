with open("data.txt", "r") as data_file:
    lines = data_file.readlines()

non_empty_lines = [line for line in lines if line.strip() != ""]

with open("data.txt", "w") as data_file:
    data_file.writelines(non_empty_lines)

print("Порожні рядки видалено з файлу data.txt")