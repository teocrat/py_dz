my_list = []
sum_list = []
my_list_1 = []
sum_list_1 = []

for i in range(1, 1000, 2):
    my_list.append(i ** 3)
    my_list_1.append(i ** 3 + 17)

for count_1 in range(len(my_list)):
    dig = 0
    n = my_list[count_1]
    while n > 0:
        dig = dig + n % 10
        n = n // 10

    if dig % 7 == 0:
        sum_list.append(my_list[count_1])

for count_2 in range(len(my_list_1)):
    dig_1 = 0
    b = my_list_1[count_2]
    while b > 0:
        dig_1 = dig_1 + b % 10
        b = b // 10

    if dig_1 % 7 == 0:
            sum_list_1.append(my_list[count_2])

result_1 = 0
for count_3 in sum_list:
    result_1 += count_3

result_2 = 0
for count_4 in sum_list_1:
    result_2 += count_4

print(result_1)
print(result_2)
