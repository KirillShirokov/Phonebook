import os
from typing import List


def menu_bar(print_list: List):
    """Функция вывода в консоль меню программы"""

    for item in print_list:
        print(item)

def load_records(file_name: str):
    """Функция для загрузки записей из файла."""

    records = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                records.append(line.strip())
    return records

def save_records(records: List, file_name: str):
    """Функция для сохранения записей в файл."""

    with open(file_name, "w") as file:
        for record in records:
            file.write(record + "\n")

def display_records(records: List, page_size: int, page_number: int):
    """Функция для вывода записей c пагинацией."""

    start_index = (page_number - 1) * page_size
    end_index = page_number * page_size
    for record in records[start_index:end_index]:
        print(record)

def add_record(records: List, file_name: str):
    """Функция для добавления новой записи в справочник."""

    last_name = input(str("Введите фамилию: "))
    first_name = input(str("Введите имя: "))
    middle_name = input(str("Введите отчество: "))
    organization = input(str("Введите название организации: "))
    work_phone = input(str("Введите рабочий телефон: "))
    personal_phone = input(str("Введите личный телефон (сотовый): "))
    new_record = f"{last_name},{first_name},{middle_name},{organization},{work_phone},{personal_phone}"
    if new_record in records:
        print("Такая запись уже существует.")
    else:
        records.append(new_record)
        save_records(records, file_name)

def edit_record(records: List, file_name: str):
    """Функция для редактирования записей в справочнике."""

    last_name = input("Введите фамилию записи, которую хотите отредактировать: ")
    for i, record in enumerate(records):
        if record.startswith(last_name):
            print(f"Редактирование записи: {record}")
            new_record = input("Введите новые данные через запятую: ")
            records[i] = new_record
            save_records(records, file_name)
            print("Запись успешно отредактирована.")
    print("Запись не найдена.")

def search_records(records: List):
    """Функция для поиска записей."""

    query = str(input("Введите характеристику для поиска: "))
    results = []
    for record in records:
        if query.lower() in record.lower():
            results.append(record)
    if len(results) > 0:
        print("Результаты поиска:")
        for result in results:
            print(result)
    else:
        print("Записи не найдены.")


def main():
    """Основная функция программы."""

    file_name: str = "справочник.txt"
    records: List = load_records(file_name)
    page_size: int = 5
    page_number: int = 1
    command_list: List = ["Меню:",
                          "0. Вывод записей",
                          "1. Следующий ->",
                          "2. Предыдущий <-",
                          "3. Добавление записи",
                          "4. Редактирование записи",
                          "5. Поиск записей",
                          "6. Выход",
                         ]

    while True:
        menu_bar(command_list)
        choice = int(input("Выберите пункт меню: "))
        if choice == 0:
            display_records(records, page_size, page_number)
        elif choice == 1:
            page_number += 1
            display_records(records, page_size, page_number)
        elif choice == 2:
            if page_number > 1:
                page_number -= 1
                display_records(records, page_size, page_number)
        elif choice == 3:
            add_record(records, file_name)
        elif choice == 4:
            edit_record(records, file_name)
        elif choice == 5:
            search_records(records)
        elif choice == 6:
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
