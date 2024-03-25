import Notepad  # Импорт модуля Notepad

def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')  # Открытие файла notes.csv в режиме записи
    file.seek(0)  # Перемещение указателя на начало файла
    file.close()  # Закрытие файла
    file = open("notes.csv", mode=mode, encoding='utf-8')  # Открытие файла notes.csv в заданном режиме
    for notes in array:  # Цикл по всем заметкам в массиве
        file.write(Notepad.Note.to_string(notes))  # Запись заметки в файл
        file.write('\n')  # Добавление новой строки после каждой заметки
    file.close  # Закрытие файла

def read_file():
    try:
        array = []  # Создание пустого массива для хранения заметок
        file = open("notes.csv", "r", encoding='utf-8')  # Открытие файла notes.csv в режиме чтения
        notes = file.read().strip().split("\n")  # Чтение заметок из файла и разделение их по строкам
        for n in notes:  # Цикл по всем заметкам
            split_n = n.split(';')  # Разделение заметки на части по символу ';'
            note = Notepad.Note(
                id=split_n[0], title=split_n[1], body=split_n[2], date=split_n[3])  # Создание объекта заметки
            array.append(note)  # Добавление заметки в массив
    except Exception:
        print('Нет сохраненных заметок...')  # Вывод сообщения, если не удалось прочитать заметки
    finally:
        return array  # Возвращение массива заметок