from tabulate import tabulate
import csv
import time
from datetime import datetime

#Все заметки
def all_notes():
    notes = []
    with open('daily_planner.csv', 'r', encoding='UTF-8') as file:
        reading_file = csv.reader(file, delimiter=';')
        for row in reading_file:
            try:
                heading = row[1][:50] + '\n' + \
                    row[1][50:] if len(row[1]) > 50 else row[1]
                comment = row[2][:50] + '\n' + \
                    row[2][50:] if len(row[2]) > 50 else row[2]
                date_creation = row[3] if row[3] else ''
                date_change = row[4] if row[4] else ''
                notes.append([row[0], heading, comment, date_creation, date_change])
            except IndexError:
                notes.append(['', '', '', '', ''])
    print("\nВсе заметки: \n")
    print(tabulate(notes, headers=['\033[91mID', 'Заголовок', 'Комментарий', 'Дата/время создания заметки', 'Дата/время изменения заметки\033[0m'], tablefmt="simple", stralign="center"))

#Получение id следующей записи
def next_record_id():
    with open("daily_planner.csv", "r", encoding='UTF-8') as file:
        reading_file = csv.reader(file, delimiter=';')
        id_list = [int(row[0].replace('.', '')) for row in reading_file if row]
        return max(id_list) + 1 if id_list else 1

#Добавление заметок
def adding_entry(heading, comment):
    id = next_record_id()
    date_creation = time.strftime("%d.%m.%Y %H:%M:%S %a", time.localtime())
    with open("daily_planner.csv", "a", encoding='UTF-8', newline='') as file:
        saving_data = csv.writer(file, delimiter=';')
        saving_data.writerow([id, heading, comment, date_creation, ''])

#Удаление заметок
def deleting_entry(delete):
    notes = []
    with open("daily_planner.csv", "r", encoding='UTF-8') as file:
        reader_file = csv.reader(file, delimiter=";")
        for row in reader_file:
            if int(row[0]) != delete:
                notes.append(row)
    for i in range(len(notes)):
        notes[i][0] = str(i+1)
    with open("daily_planner.csv", "w", encoding='UTF-8', newline='') as file:
        saving_file = csv.writer(file, delimiter=";")
        saving_file.writerows(notes)

#Редактирование заметок
def changing_entry(id, heading, comment):
    notes = []
    with open("daily_planner.csv", "r", encoding='UTF-8') as file:
        reader_file = csv.reader(file, delimiter=';')
        for row in reader_file:
            if int(row[0]) == id:
              if heading is not None:
                row[1] = heading
              if comment is not None:
                row[2] = comment
              row[4] = time.strftime("%d.%m.%Y %H:%M:%S %a")
            notes.append(row)
    
    with open("daily_planner.csv", "w", encoding='UTF-8', newline='') as file:
        writer_file = csv.writer(file, delimiter=';')
        writer_file.writerows(notes)

#Выбор заметок по дате 
def selection_by_date(date):
  search_result = []
  with open("daily_planner.csv", "r", encoding='UTF-8') as file:
    reading_file = csv.reader(file, delimiter=";")
    for row in reading_file:
      adding_date = datetime.strptime(row[3], '%d.%m.%Y %H:%M:%S %a')
      if adding_date.strftime("%d.%m.%Y") == date:
        search_result.append(row)
  return search_result

#Выбор заметок по id
def selection_by_id(id):
    search_result = []
    with open("daily_planner.csv", "r", encoding='UTF-8') as file:
        reading_file = csv.reader(file, delimiter=";")
        for row in reading_file:
            if row[0] == id:
                search_result.append(row)
    return search_result

