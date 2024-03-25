# Импорт функции из модуля function под именем f
import function as f
# Импорт модуля ui
import ui

# Определение функции run
def run():
    # Инициализация переменной input_from_user пустой строкой
    input_from_user = ''
    # Цикл продолжается, пока пользователь не введет '7'
    while input_from_user != '7':
        # Вызов функции menu из модуля ui
        ui.menu()
        # Получение ввода от пользователя
        input_from_user = input().strip()
        # Если пользователь ввел '1'
        if input_from_user == '1':
            # Вызов функции show из модуля f с аргументом 'all'
            f.show('all')
        # Если пользователь ввел '2'
        if input_from_user == '2':
            # Вызов функции add из модуля f
            f.add()
        # Если пользователь ввел '3'
        if input_from_user == '3':
            # Вызов функции show из модуля f с аргументом 'all'
            f.show('all')
            # Вызов функции id_edit_del_show из модуля f с аргументом 'del'
            f.id_edit_del_show('del')
        # Если пользователь ввел '4'
        if input_from_user == '4':
            # Вызов функции show из модуля f с аргументом 'all'
            f.show('all')
            # Вызов функции id_edit_del_show из модуля f с аргументом 'edit'
            f.id_edit_del_show('edit')
        # Если пользователь ввел '5'
        if input_from_user == '5':
            # Вызов функции show из модуля f с аргументом 'date'
            f.show('date')
        # Если пользователь ввел '6'
        if input_from_user == '6':
            # Вызов функции show из модуля f с аргументом 'id'
            f.show('id')
            # Вызов функции id_edit_del_show из модуля f с аргументом 'show'
            f.id_edit_del_show('show')
        # Если пользователь ввел '7'
        if input_from_user == '7':
            # Вызов функции goodbuy из модуля ui
            ui.goodbuy()
            # Прерывание цикла
            break