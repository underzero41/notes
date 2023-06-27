import csv
import datetime

def save_note():
    indicator = input("Введите индикатор заметки: ")
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('notes.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([indicator, title, body, current_time])
    
    print("Заметка сохранена успешно.")

def read_notes():
    with open('notes.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Индикатор:", row[0])
            print("Заголовок:", row[1])
            print("Текст:", row[2])
            print("Дата/Время:", row[3])
            print()

def add_note():
    save_note()

def edit_note():
    indicator = input("Введите индикатор заметки для редактирования: ")
    rows = []
    with open('notes.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == indicator:
                row[1] = input("Введите новый заголовок заметки: ")
                row[2] = input("Введите новый текст заметки: ")
                row[3] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            rows.append(row)

    with open('notes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)    
    print("Заметка успешно изменена.")

def delete_note():
    indicator = input("Введите индикатор заметки для удаления: ")
    rows = []
    with open('notes.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != indicator:
                rows.append(row)

    with open('notes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Заметка успешно удалена.")

def main():
    while True:
        print("\n" + "="*20 + " Заметки " + "="*20)
        print("1. Сохранить заметку")
        print("2. Просмотреть все заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти\n")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Неправильный выбор. Повторите попытку.")

if __name__ == "__main__":
    main()