from src.database import add_employee, add_vacancy, get_employees, get_vacancies


def data_menu():
    while True:
        print("\nМеню работы с данными:")
        print("1. Добавить сотрудника")
        print("2. Добавить вакансию")
        print("3. Показать всех сотрудников")
        print("4. Показать все вакансии")
        print("5. Вернуться в главное меню")

        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите имя сотрудника: ")
            position = input("Введите должность: ")
            add_employee(name, position)

        elif choice == "2":
            title = input("Введите название вакансии: ")
            salary = int(input("Введите зарплату: "))
            add_vacancy(title, salary)

        elif choice == "3":
            employees = get_employees()
            if employees:
                print("Сотрудники:")
                for emp in employees:
                    print(emp)
            else:
                print("Сотрудников нет.")

        elif choice == "4":
            vacancies = get_vacancies()
            if vacancies:
                print("Вакансии:")
                for vac in vacancies:
                    print(vac)
            else:
                print("Вакансий нет.")

        elif choice == "5":
            break
        else:
            print("Неверный ввод, попробуйте снова.")
