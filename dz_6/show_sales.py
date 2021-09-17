from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    tmp = f.read()
    tmp = tmp.strip()
    line = tmp.split('\n')
if len(argv) > 1:
    if len(argv) == 2:
        st, = map(int, argv[1:])
        if st >= 1:
            for i in line[st - 1:]:
                print(i)
    if len(argv) == 3:
        st, en = map(int, argv[1:])
        if st >= 1 and en >= 1:
            for i in line[st - 1:en]:
                print(i)


else:
    for i in line:
        print(i)
