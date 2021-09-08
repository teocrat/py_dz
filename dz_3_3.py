def thesaurus(*args):
    names = {}
    for n in sorted(args):
        key = n[0]
        if key in names:
            names[key] += [n]
        else:
            names[key] = [n]
    return names


print(thesaurus('Петя', 'Вася', 'Дима', 'Вова', 'Сергей', 'Святослав', 'John', 'Kitty', 'Jacob', 'Kristobal'))





