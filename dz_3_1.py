word_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
             'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять', 'One': 'Один', 'Two': 'Два',
             'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять', 'Six': 'Шесть',
             'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}


def num_translate(word_num):
    return print(word_dict.get(word_num))


word_num = input("Введите цифру на английском: ")
num_translate(word_num)
