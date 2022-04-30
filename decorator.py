from datetime import datetime


def log_decor(some_function):
    def log_it(*args, **kwargs):
        date_time = datetime.now().strftime('%d-%m-%y %H:%M')
        funct_name = some_function.__name__
        result = some_function(*args, **kwargs)
        with open('deco_log.txt', 'a', encoding='utf-8') as f:
            f.write(f'Вызвана функция: {funct_name}\n'
                    f'День и время: {date_time}\n'
                    f'С аргументами: {args} и {kwargs}\n'
                    f'И результатом: {result}')
            return result
    return log_it
