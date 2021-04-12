def thesaurus_adv(*args):
    names_list = list(args)

    letters_set = set()  # создаем пустое множество

    names_lists_list = []
    for name in names_list:
        letters_set.add((name[0], name.split(' ')[1][0]))
        list_tuples = list(letters_set)

        names_lists_list = []
        for letter_tuple in list_tuples:
            def accepted(el_name):
                return el_name.startswith(letter_tuple[0]) and el_name.split(' ')[1].startswith(letter_tuple[1])

            name_list = filter(accepted, names_list)
            name_list = list(name_list)
            names_lists_list.append(name_list)

    names_filter_dict = {}
    names_dict_list = {}
    for name_lst in names_lists_list:
        if name_lst[0].split(' ')[1][0] in names_filter_dict.keys():
            names_dict_list.setdefault(name_lst[0][0], name_lst)
            names_filter_dict[name_lst[0].split(' ')[1][0]].update(names_dict_list)

        else:
            names_filter_dict[name_lst[0].split(' ')[1][0]] = {name_lst[0][0]: name_lst}

    print(names_filter_dict)
    return names_filter_dict  # для дальнейшей сортировки словаря необходимо вернуть словарь как результат работы
    # функции


for_sorted = thesaurus_adv('Василий Петров', 'Сергей Иванов', 'Александр Сидоров', 'Алексей Савельев',
                           'Владимир Пушкин', 'Светлана Иевлева', 'Валентина Самойлова')
list_keys = list(for_sorted.keys())
list_keys.sort()
for i in list_keys:
    #  Выводим на экран отсортированный словарь в формате key: value
    print(i, ':', for_sorted[i])
