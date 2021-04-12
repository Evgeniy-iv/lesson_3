translate_dict_1 = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
                    'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
                    'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(num_key):
    if num_key not in translate_dict_1:
        None
    else:
        print(translate_dict_1[num_key])


num_translate('one')


# задание 2 - функция выводит на экран числительное по русски с большой буквы, если оно поступало в качестве аргумента с
# большой буквы по английски
def num_translate_1(num_key):
    if num_key.lower() not in translate_dict_1:
        None
    elif num_key == num_key.title():
        print(translate_dict_1[num_key.lower()].title())
    else:
        print(translate_dict_1[num_key.lower()])


num_translate_1('Two')
