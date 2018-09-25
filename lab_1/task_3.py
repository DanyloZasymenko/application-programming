class Error(Exception):
    pass


class NegativeValueError(Error):
    pass


class ZeroValueError(Error):
    pass


def modulus(a, b):
    try:
        a = int(a)
        b = int(b)
        if a < 0 or b < 0:
            raise NegativeValueError()
        elif b == 0:
            raise ZeroValueError()
        return int(a) % int(b) == 0
    except NegativeValueError:
        print('Input values cannot be negative')
    except ZeroValueError:
        print('b cannot be 0')


a = input("enter a:")
b = input("enter b:")
print(str(modulus(a, b)))
