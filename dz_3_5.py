nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice, randrange


def get_jokes(n):
    """Функция печатает случайные шутки, собранные из трех списков без флага повтора
    n - количество шуток
    joke - список шуток
    """
    joke = []
    while n and len(min(nouns, adverbs, adjectives)):
        joke.append(f"{choice(nouns)}, {choice(adverbs)}, {choice(adjectives)}")
        n -= 1
    return print(joke)


get_jokes(5)

print('*' * 100)

f = None


def get_jokes(n, f):
    """Функция печатает случайные шутки, собранные из трех списков c флагом повтора
    n - количество шуток
    f - флаг повтора
    joke - список шуток
    """
    f = input("Вы хотите уникальные шутки: (y/n) ")
    if f == 'y':
        f = True
    else:
        f = False
    joke = []
    while n and len(min(nouns, adverbs, adjectives)):
        i = randrange(len(min(nouns, adverbs, adjectives)))
        if f:
            joke.append(f"{nouns.pop(i)} {adverbs.pop(i)}  {adjectives.pop(i)}")
        else:
            joke.append(f"{choice(nouns)} {choice(adverbs)}  {choice(adjectives)}")
        n -= 1

    return print(joke)


get_jokes(100, f)
