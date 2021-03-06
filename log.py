from datetime import datetime
import hashlib

path = 'Log.txt'

#задание №2
def my_decorator(old_function):
    def decor(get_path):
        def new_function(*args, **kwargs):
            f = open('Log.txt', 'a', encoding='utf8')
            f.write(f'Дата и время записи функции: {datetime.now().strftime("%d %B %Y  time %H:%M:%S")}\n')
            f.write(f'Имя функции: {get_path.__name__}\n')
            f.write(f'Аргументы: {args}, {kwargs}\n')
            result = get_path(*args, **kwargs)
            f.write(f'Результат: {result}\n')
            f.write(f'____________________\n')
            return result
        return new_function
    return decor

@my_decorator(path)
def get_path():
    with open(path, 'w', encoding='utf-8') as f:
        for i in f:
            yield hashlib.md5(i.encode()).hexdigest()


old_function = get_path()
