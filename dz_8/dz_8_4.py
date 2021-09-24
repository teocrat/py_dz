from functools import wraps


def val_checker(lam):
    def _checker(func):
        @wraps(func)
        def wrapper(*argv):

            if lam(*argv):
                print(func(*argv))

            else:
                raise ValueError('wrong val: ' + str(*argv))

        return wrapper

    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


if __name__ in '__main__':
    print(help(calc_cube))
    calc_cube(5)
    calc_cube(-5)
    
