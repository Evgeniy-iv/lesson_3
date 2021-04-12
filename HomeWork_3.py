def thesaurus(*args):
    letters_set = set()  # создаем пустое множество
    for name in args:  # используем цикл для добавление первых букв полученных в функцию имен в множество
        # - в множестве все значения уникальны
        letters_set.add(name[0])
    name_list = list(args)
    names_filter_dict = {}  # создаем пустой словарь
    for letter in letters_set:
        def accepted(startswith_letter):
            return startswith_letter.startswith(letter)  # используем функцию для передачи буквы
            # из множества в функцию filter

        names_filter = filter(accepted, name_list)
        names_filter_dict[letter] = (list(names_filter))

    print(names_filter_dict)  # результат работы функции thesaurus - вывод словаря на экран
    return names_filter_dict  # для дальнейшей сортировки словаря необходимо вернуть словарь как результат работы
    # функции


for_sorted = thesaurus('Василий', 'Сергей', 'Александр', 'Алексей', 'Владимир',
                       'Станислав')  # вызыватся функция thesaurus с
# произвольным количеством параметров (Имен), результат работы функции присваивается переменной for_sorted,
# для сортировки

# сортируем словарь по ключам
list_keys = list(for_sorted.keys())
list_keys.sort()
for i in list_keys:
    #  Выводим на экран отсортированный словарь в формате key: value
    print(i, ':', for_sorted[i])
