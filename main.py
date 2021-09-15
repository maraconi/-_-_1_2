from datetime import datetime

#задание №1
def my_decorator(old_function):
    def new_function(*args, **kwargs):
        f = open('Log.txt', 'a', encoding='utf8')
        f.write(f'Дата и время записи функции: {datetime.now().strftime("%d %B %Y  time %H:%M:%S")}\n')
        f.write(f'Имя функции: {old_function.__name__}\n')
        f.write(f'Аргументы: {args}, {kwargs}\n')
        result = old_function(*args, **kwargs)
        f.write(f'Результат: {result}\n')
        f.write(f'____________________\n')
        return result
    return new_function

@my_decorator
def get_logger():
    with open('Log.txt', 'w', encoding='utf-8') as f:
        f.write(f'Записываем данные в файл: \n')

old_function = get_logger()

