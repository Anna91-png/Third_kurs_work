from src.database import create_tables
from src.menu import data_menu  # подменю вынесли в отдельный файл для удобства


if __name__ == "__main__":
    print("Добро пожаловать в систему вакансий! \n")

    while True:
        print("\nВыберите действие:")
        print("1. Создать базу и загрузить данные")
        print("2. Вывести меню работы с данными")
        print("3. Выйти")

        user_choice = input("Введите номер действия: ")

        if user_choice == "1":
            create_tables()

        elif user_choice == "2":
            data_menu()

        elif user_choice == "3":
            print("Выход из программы")
            break

        else:
            print("Неверный номер. Введите снова.")
