import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


# функция возвращающая n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого),
# аргументы позиционные: количество шуток(number_of_jokes) и тип функции(choice_type) выбирающая слово либо с
# возможным повторением либо без повторения(random.choice и random.sample соответственно)
def get_jokes(number_of_jokes, choice_type):
    random_nouns = (choice_type(nouns, number_of_jokes))
    random_adverbs = (choice_type(adverbs, number_of_jokes))
    random_adjectives = (choice_type(adjectives, number_of_jokes))
    for noun, adverb, adjective in zip(random_nouns, random_adverbs, random_adjectives):
        print(f'{noun}, {adverb}, {adjective}')


get_jokes(1, random.sample)


# тоже самое, но с именнованными аргументами:

def get_jokes_1(**kwargs):
    random_nouns = kwargs['choice_type'](nouns, kwargs['number_of_jokes'])
    random_adverbs = kwargs['choice_type'](adverbs, kwargs['number_of_jokes'])
    random_adjectives = kwargs['choice_type'](adjectives, kwargs['number_of_jokes'])
    for noun, adverb, adjective in zip(random_nouns, random_adverbs, random_adjectives):
        print(f'{noun}, {adverb}, {adjective}')


print('\nРезультат работы функции с именнованными аргументами: \n')
get_jokes_1(number_of_jokes=5, choice_type=random.sample)
