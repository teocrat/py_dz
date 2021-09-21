import json

# Для проверки, когда список имен больше списка хобби:

users_add = '''Иванов,Иван,Иванович\nАлексеев,Алексей,Петрович\nМельников,Владимир,Владимирович\nБарсуков,Евгений,Павлович
Семенов,Сергей,Васильевич\nРыжов,Вадим,Константинович\nБабич,Кирилл,Иванович\nСергеев,Сергей,Сергеевич\nКушнир,Василий,Андреевич\nПушкин,Илья,Федорович\nМихеев,Борис,Михайлович\n'''
with open('users.csv', 'a', encoding='utf-8') as f:
    f.write(users_add)

us_hob = {}

with open('users.csv', 'r', encoding='utf-8') as f:
    users = f.read()
with open('hobby.csv', 'r', encoding='utf-8') as f_1:
    hobby = f_1.read()

users = users.strip()
users = users.replace(',', ' ')
users = users.split('\n')
hobby = hobby.split('\n')

if len(users) >= len(hobby):
    for i in range(len(hobby)):
        k = users[i]
        if i >= len(hobby) - 1:
            v = None
        else:
            v = hobby[i]
        us_hob.setdefault(k, v)
else:
    exit(1)

print(us_hob)

f = json.dumps(us_hob, ensure_ascii=False, indent=4)
with open('us_hobby.csv', 'w', encoding='utf-8') as file:
    file.write(f)
# для проверки записанного файла
with open('us_hobby.csv', 'r', encoding='utf-8') as file:
    f = file.read()
a = json.loads(f)

print('-' * 120)

print(a)
