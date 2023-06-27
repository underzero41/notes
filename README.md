# intermediate_certification

This is an intermediate control work on the block of specialization. It includes two applications: notes and toy shop.

## Заметки
Мне было дано задание
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.Например:
```
python notes.py add --title "новая заметка" –msg "тело новой заметки"
```
Или так:
```
python note.py
Введите команду: add
Введите заголовок заметки: новая заметка
Введите тело заметки: тело новой заметки
Заметка успешно сохранена
Введите команду:
```
При чтении списка заметок реализовать фильтрацию по дате.

## Notes
I was given a task
Implement a note console application, with saving, reading,
adding, editing and deleting notes. The note should
contain an ID, title, body of the note, and date/time of creation, or
the note was last modified. Saving notes must be done in
json format or csv format (field separation is recommended to be done through
semicolon). User interface implementation student can
do as it is more convenient for him, you can do it as program launch parameters
(command, data), can be done as a command request from the console and
subsequent data entry, somehow else, at the discretion of the student. For example:
```
python notes.py add --title "new note" –msg "new note body"
```
Or like this:
```
python note.py
Enter the command: add
Enter note title: new note
Enter note body: new note body
Note saved successfully
Enter the command:
```
When reading a list of notes, implement filtering by date.
