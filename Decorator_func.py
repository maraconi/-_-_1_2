from datetime import datetime
import hashlib
import requests

path = 'Log.txt'

#задание №3
def my_decorator(old_function):
    def decor(get_path_vk):
        def new_function(*args, **kwargs):
            f = open(path, 'a', encoding='utf8')
            f.write(f'Дата и время записи функции: {datetime.now().strftime("%d %B %Y  time %H:%M:%S")}\n')
            f.write(f'Имя функции: {get_path_vk.__name__}\n')
            f.write(f'Аргументы: {args}, {kwargs}\n')
            result = get_path_vk(*args, **kwargs)
            f.write(f'Результат: {result}\n')
            f.write(f'____________________\n')
            return result
        return new_function
    return decor

@my_decorator(path)
def get_path_vk(url):
    res = requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        for i in f:
            yield hashlib.md5(i.encode()).hexdigest()
    return res.text

res = get_path_vk('https://cloud-api.yandex.net/v1/disk/resources/')
print(res)