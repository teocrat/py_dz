init_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for count in init_list:
    nam = count.split()[-1]
    print('Привет,', nam.title())

print('_' * 70)
init_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
name = []
for item in init_list:
    name.append(item.split())

first_name = name.pop()[-1]
print('Здравствуйте,', first_name.title())
second_name = name.pop()[-1]
print('Как дела,', second_name.title())
third_name = name.pop()[-1]
print('Приветствую Вас,', third_name.title())
fourth_name = name.pop()[-1]
print('Привет,', fourth_name.title())
