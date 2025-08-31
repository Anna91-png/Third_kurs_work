from src.database import create_tables, populate_database, get_employees, get_vacancies

def data_menu():
    while True:
        print("\nМеню работы с данными:")
        print("1. Добавить компанию")
        print("2. Добавить вакансию")
        print("3. Показать все компании")
        print("4. Показать все вакансии")
        print("5. Вернуться в главное меню")

        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Название компании: ")
            from src.database import add_employee
            add_employee(name)
            print("Компания добавлена!")

        elif choice == "2":
            title = input("Название вакансии: ")
            salary = int(input("Зарплата: "))
            company_id = int(input("ID компании: "))
            from src.database import add_vacancy
            add_vacancy(title, salary, company_id)
            print("Вакансия добавлена!")

        elif choice == "3":
            companies = get_employees()
            if companies:
                for c in companies:
                    print(f"ID: {c[0]}, Название: {c[1]}")
            else:
                print("Компаний нет.")

        elif choice == "4":
            vacancies = get_vacancies()
            if vacancies:
                for v in vacancies:
                    print(f"ID: {v[0]}, Название: {v[1]}, Зарплата: {v[2]}, Компания: {v[3]}")
            else:
                print("Вакансий нет.")

        elif choice == "5":
            break
        else:
            print("Неверный номер. Попробуйте снова.")


if __name__ == "__main__":
    print("Добро пожаловать в систему вакансий!\n")

    while True:
        print("\nВыберите действие:")
        print("1. Создать базу и загрузить данные")
        print("2. Вывести меню работы с данными")
        print("3. Выйти")

        user_choice = input("Введите номер действия: ")

        if user_choice == "1":
            create_tables()
            populate_database()
        elif user_choice == "2":
            data_menu()
        elif user_choice == "3":
            print("Выход из программы")
            break
        else:
            print("Неверный номер. Введите снова.")
