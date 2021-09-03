# вариант 1
print('вариант 1', '_' * 70, )
this_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, item in enumerate(this_list):
    item = item.replace('5', '"05"')
    item = item.replace('17', '"17"')
    item = item.replace('+"05"', '"+05"')
    this_list[i] = item

message = ' '.join(this_list)

print(message)

# вариант 2
print('вариант 2', '_' * 70, )

this_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message_list = []

for count in this_list:
    if count.replace('+', '').replace('-', '').isdigit():
        if count.isdigit():
            message_list.append(f'"{int(count):02d}"')
        else:
            message_list.append(f'"{count[0]}{int(count[1:]):02d}"')
    else:
        message_list.append(count)

print(' '.join(message_list))
