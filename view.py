import csv
from tabulate import tabulate

# Основное меню
def menu_output():
  print("\nМеню пользователя:\n")
  menu = [
    "1. Все заметки",
    "2. Добавление заметок",
    "3. Удаление заметок",
    "4. Изменение заметок",
    "5. Выбор заметок по дате добавления",
    "6. Выбор заметок по id",
    "7. Выход"
    ]
  for item in menu:
    print(item)
  return menu

# Выбор пункта меню, проверка ввода
def user_selection(menu):
    while True:
        try:
            choice = int(input("\nВыбор пункта меню: "))
            if choice > 0 and choice <= len(menu):
                return choice
            else:
                print("\nОшибка! Пожалуйста, введите число от 1 до", len(menu))
        except ValueError:
            print("\nОшибка! Пожалуйста, введите число от 1 до", len(menu))

#Добавление заметок
def adding_notes():
    print("\nВы выбрали добавление заметок. Заполните необходимые поля:")
    header = input("\nЗаголовок заметки: ")
    comment = input("Комментарий заметки: ")
    return header, comment

#Удаление заметок
def delete_notes(file):
    print("\nУдалить заметку: ")
    while True:
        try:
            id_number = int(input("\nВведите номер заметки для удаления:"))
            break
        except ValueError:
            print("\nОшибка! Пожалуйста, введите число!")

    notes = []
    reading_file = csv.reader(file, delimiter=";")
    for row in reading_file:
        notes.append(row)

    if id_number not in [int(note[0]) for note in notes]:
        print("Ошибка. Заметка отсутствует в списке!")
        return None
    else:
        notes = [note for note in notes if int(note[0]) != id_number]
        print("\nЗаметка успешно удалена!")
        return id_number

#Редактирование заметок 
def editing_notes(file):
    print("\nРедактировать заметку: ")
    try:
        id = int(input("\nВведите номер заметки для редактирования: "))
    except ValueError:
        print("\nОшибка! Пожалуйста, введите число!")
        return None
    
    notes = []
    reading_file = csv.reader(file, delimiter=";")
    for row in reading_file:
        notes.append(row)
      
    heading = None
    comment = None
    if id not in [int(note[0]) for note in notes]:
        print("Ошибка. Заметка отсутствует в списке!")
        return None
    else:
        notes = [note for note in notes if int(note[0]) != id]
        heading = input("\nРедактировать заголовок: ") or None
        comment = input("Редактировать комментарий: ") or None
        print("\nЗаметка успешно отредактирована!")
    return id, heading, comment

#Ввод даты для поиска
def date_added():
    print("Выбор заметок по дате добавления: ")
    enter_date = input("\nВведите дату, формат ввода дд.мм.гггг: ")
    return enter_date
  
#Ввод id для поиска
def id_added():
    print("Выбор заметок по id: ")
    enter_id = input("\nВведите id: ")
    return enter_id

#Вывод заметок по результату поиска
def output_notes(result):
  print()
  print(tabulate(result, headers=['\033[91mID', 'Заголовок', 'Комментарий', 'Дата/время создания заметки', 'Дата/время изменения заметки\033[0m'], tablefmt="simple", stralign="center"))

#Завершение работы
def work_completed():
    print("\nРабота завершена")