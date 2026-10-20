def check_number():
    """1. Если введенное число больше 7, то вывести 'Hello'."""
    try:
        num = float(input("Введите число: "))
        if num > 7:
            print("Hello")
    except ValueError:
        print("Ошибка: Пожалуйста, введите корректное число.")


def check_name():
    """2. Если введенное имя совпадает с 'John', то вывести 'Hello, John', иначе — 'There is no such name'."""
    name = input("Введите имя: ").strip()
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")


def check_array_multiples_of_three():
    """3. На входе числовой массив, необходимо вывести элементы массива, кратные 3."""
    user_input = input("Введите числа массива через пробел: ").strip()
    if not user_input:
        print("Массив пуст.")
        return

    try:
        array = [int(x) for x in user_input.split()]
        multiples_of_three = [num for num in array if num % 3 == 0]
        print("Элементы массива, кратные 3:", multiples_of_three)
    except ValueError:
        print("Ошибка: Вводимые элементы массива должны быть целыми числами.")


def main():
    print("=== ЗАДАНИЕ 1: Проверка числа ===")
    check_number()
    print("\n=== ЗАДАНИЕ 2: Проверка имени ===")
    check_name()
    print("\n=== ЗАДАНИЕ 3: Фильтрация массива ===")
    check_array_multiples_of_three()


if __name__ == "__main__":
    main()
