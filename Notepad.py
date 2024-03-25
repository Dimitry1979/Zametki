from datetime import datetime
import uuid

# Определение класса Note
class Note:
    # Инициализация объекта класса Note
    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id  # уникальный идентификатор заметки
        self.title = title  # заголовок заметки
        self.body = body  # текст заметки
        self.date = date  # дата создания заметки

    # Метод для получения id заметки
    def get_id(note):
        return note.id

    # Метод для получения заголовка заметки
    def get_title(note):
        return note.title

    # Метод для получения текста заметки
    def get_body(note):
        return note.body

    # Метод для получения даты создания заметки
    def get_date(note):
        return note.date

    # Метод для установки нового id заметки
    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    # Метод для установки нового заголовка заметки
    def set_title(note, title):
        note.title = title

    # Метод для установки нового текста заметки
    def set_body(note, body):
        note.body = body

    # Метод для установки новой даты создания заметки
    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    # Метод для преобразования заметки в строку
    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    # Метод для отображения заметки в удобочитаемом формате
    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date