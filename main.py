import json
from datetime import datetime

def dec_logger(file_path, max_size):

    def dec_logger_(old_function):
        log_dict = {}

        def new_function(*args, **kwargs):
            time_start_func = str(datetime.now())
            result = old_function(*args, **kwargs)

            if len(log_dict) > max_size:
                log_dict.pop(list(log_dict)[0])
                print('Превышен max размер словаря, поэтому далён начальный элемент и добавлен текущий.')

            log_dict[time_start_func] = f"функция {old_function.__name__} вызвана с аргументами {args}, результат = {result}."
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(log_dict, file, ensure_ascii=False, indent=4)
                print('Запись в файл прошла успешно.')

            return result
        return new_function
    return dec_logger_


@dec_logger(file_path='res_decor.json', max_size=2)
def do_linear_list(list_):
    linear_list = []
    for element in list_:
        if type(element) != list:
            linear_list.append(element)
        else:
            for i in do_linear_list(element):
                linear_list.append(i)
    print(f"Выполнилась функция do_linear_list.")
    return linear_list


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None]]

    print(do_linear_list(nested_list))