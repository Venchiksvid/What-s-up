def load_shopping_list(filename):
    shopping_list = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                item, quantity = line.strip().split(', ')
                shopping_list[item] = int(quantity)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено. Буде створено новий файл.")
    return shopping_list

def save_shopping_list(filename, shopping_list):
    with open(filename, 'w') as file:
        for item, quantity in shopping_list.items():
            file.write(f"{item}, {quantity}\n")

def add_item(shopping_list):
    item = input("Введіть назву продукту: ")
    quantity = int(input("Введіть кількість: "))
    if item in shopping_list:
        shopping_list[item] += quantity
    else:
        shopping_list[item] = quantity

def view_list(shopping_list):
    if shopping_list:
        print("Поточний список покупок:")
        for item, quantity in shopping_list.items():
            print(f"{item}: {quantity}")
    else:
        print("Список покупок порожній.")

def edit_item(shopping_list):
    item = input("Введіть назву продукту для редагування: ")
    if item in shopping_list:
        quantity = int(input(f"Введіть нову кількість для {item}: "))
        shopping_list[item] = quantity
    else:
        print(f"Продукт {item} не знайдено у списку.")

def delete_item(shopping_list):
    item = input("Введіть назву продукту для видалення: ")
    if item in shopping_list:
        del shopping_list[item]
        print(f"Продукт {item} видалено зі списку.")
    else:
        print(f"Продукт {item} не знайдено у списку.")

def main():
    filename = 'shopping_list.txt'
    shopping_list = load_shopping_list(filename)

    while True:
        print("\nМеню:")
        print("1. Додати продукт")
        print("2. Переглянути список")
        print("3. Редагувати продукт")
        print("4. Видалити продукт")
        print("5. Зберегти та вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            view_list(shopping_list)
        elif choice == '3':
            edit_item(shopping_list)
        elif choice == '4':
            delete_item(shopping_list)
        elif choice == '5':
            save_shopping_list(filename, shopping_list)
            print("Зміни збережено. Вихід з програми.")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()