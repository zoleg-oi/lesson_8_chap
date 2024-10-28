# Try и Except

def add_everything_up(a, b):
    try:
        result = round(a + b,3)
        return result
    except TypeError:
        if isinstance(a, str) != True:
            a = str(a)
        if isinstance(b, str) != True:
            b = str(b)
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
