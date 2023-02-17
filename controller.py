import view
import model

def main():
    # Открытие меню
    menu = view.menu_output()
    choice = view.user_selection(menu)
    menu_item(choice)

#Обработчик запросов 
def menu_item(choice):
    while True:
        if choice == 1: 
            model.all_notes()
        
        elif choice == 2:
            header, comment = view.adding_notes()
            model.adding_entry(header, comment)
            model.all_notes()
          
        elif choice == 3:
          with open("daily_planner.csv", "r", encoding='UTF-8') as file:
            delete = view.delete_notes(file)
            model.deleting_entry(delete)
          
        elif choice == 4:
          with open("daily_planner.csv", "r", encoding='UTF-8') as file:
            result = view.editing_notes(file)
            if result is not None:
              id, heading, comment = result
              model.changing_entry(id, heading, comment)
            model.all_notes()
          
        elif choice == 5:
           date = view.date_added()
           result = model.selection_by_date(date)
           view.output_notes(result)
           
        elif choice == 6:
          id = view.id_added()
          result = model.selection_by_id(id)
          view.output_notes(result)
          
        elif choice == 7:
          view.work_completed()
          break
        menu = view.menu_output()
        choice = view.user_selection(menu)