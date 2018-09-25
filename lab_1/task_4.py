class Error(Exception):
    pass


class NoSimpleDigits(Error):
    pass


def generatesimpledigits(a, b):
    try:
        a = int(a)
        b = int(b)
        result = []
        if a >= b:
            raise NoSimpleDigits
        while a <= b:
            result.append(a)
            a += 1
        return result
    except NoSimpleDigits:
        print('no simple digits')


a = input("enter a:")
b = input("enter b:")
print(generatesimpledigits(a, b))
