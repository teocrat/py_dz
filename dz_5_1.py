def odd_numbers():
    for num in range(1, 16, 2):
        yield num


odd_num = odd_numbers()

print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))