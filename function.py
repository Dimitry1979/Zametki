import file_operation  # Импорт модуля для работы с файлами
import Notepad  # Импорт модуля Notepad
import ui  # Импорт пользовательского интерфейса

number = 6  # Минимальное количество символов в тексте заметки

def add():
    note = ui.create_note(number)  # Создание новой заметки
    array = file_operation.read_file()  # Чтение файла
    for notes in array:  # Перебор всех заметок в файле
        if Notepad.Note.get_id(note) == Notepad.Note.get_id(notes):  # Если ID новой заметки совпадает с ID существующей заметки
            Notepad.Note.set_id(note)  # Установить новый ID для заметки
    array.append(note)  # Добавление новой заметки в массив
    file_operation.write_file(array, 'a')  # Запись массива в файл
    print('Заметка добавлена...')  # Вывод сообщения о добавлении заметки

def show(text):
    logic = True  # Логическая переменная для проверки наличия заметок
    array = file_operation.read_file()  # Чтение файла
    if text == 'date':  # Если пользователь хочет посмотреть заметки по дате
        date = input('Введите дату в формате dd.mm.yyyy: ')  # Ввод даты
    for notes in array:  # Перебор всех заметок в файле
        if text == 'all':  # Если пользователь хочет посмотреть все заметки
            logic = False  # Изменение логической переменной
            print(Notepad.Note.map_note(notes))  # Вывод всех заметок
        if text == 'id':  # Если пользователь хочет посмотреть заметку по ID
            logic = False  # Изменение логической переменной
            print('ID: ' + Notepad.Note.get_id(notes))  # Вывод ID заметки
        if text == 'date':  # Если пользователь хочет посмотреть заметки по дате
            logic = False  # Изменение логической переменной
            if date in Notepad.Note.get_date(notes):  # Если введенная дата совпадает с датой заметки
                print(Notepad.Note.map_note(notes))  # Вывод заметки
    if logic == True:  # Если ни одна заметка не была найдена
        print('Нет ни одной заметки...')  # Вывод сообщения о том, что заметок нет

def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')  # Ввод ID заметки
    array = file_operation.read_file()  # Чтение файла
    logic = True  # Логическая переменная для проверки наличия заметки с введенным ID
    for notes in array:  # Перебор всех заметок в файле
        if id == Notepad.Note.get_id(notes):  # Если введенный ID совпадает с ID заметки
            logic = False  # Изменение логической переменной
            if text == 'edit':  # Если пользователь хочет изменить заметку
                note = ui.create_note(number)  # Создание новой заметки
                Notepad.Note.set_title(notes, note.get_title())  # Изменение заголовка заметки
                Notepad.Note.set_body(notes, note.get_body())  # Изменение тела заметки
                Notepad.Note.set_date(notes)  # Изменение даты заметки
                print('Заметка изменена...')  # Вывод сообщения об изменении заметки
            if text == 'del':  # Если пользователь хочет удалить заметку
                array.remove(notes)  # Удаление заметки из массива
                print('Заметка удалена...')  # Вывод сообщения об удалении заметки
            if text == 'show':  # Если пользователь хочет посмотреть заметку
                print(Notepad.Note.map_note(notes))  # Вывод заметки
    if logic == True:  # Если заметка с введенным ID не была найдена
        print('Такой заметки нет, возможно, вы ввели неверный id')  # Вывод сообщения о том, что заметки с таким ID нет
    file_operation.write_file(array, 'a')  # Запись массива в файл