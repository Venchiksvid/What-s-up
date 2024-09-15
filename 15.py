with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

unique_lines = list(dict.fromkeys(lines))

with open("output.txt", "w") as output_file:
    output_file.writelines(unique_lines)

print("Унікальні рядки записано у файл output.txt")