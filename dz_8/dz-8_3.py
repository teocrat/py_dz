from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*argv, **kwargs):
        list_calc = [i for i in (*argv, *kwargs.values())]
        res = [f"{func.__name__}({i}:{type(i)})" for i in list_calc]
        print(*res, *func(*argv, **kwargs), sep=',\n')

    return wrapper


@type_logger
def calc_cube(*x, **y):
    list_calc = [i for i in (*x, *y.values()) if isinstance(i, int) or isinstance(i, float)]
    return [n ** 3 for n in list_calc]


calc_cube(3, 5, 7, 9.9, yd=55, str='der')
print(help(calc_cube))
