tutors = [
    'Иван ', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
]

classes = [
    '9A', '7B', '9Б', '9В', '9A'
]


def gen_tutor():
    for i in range(len(tutors)):
        if i >= len(classes):
            yield (tutors[i], None)
        else:
            yield (tutors[i], classes[i])


gen = gen_tutor()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
