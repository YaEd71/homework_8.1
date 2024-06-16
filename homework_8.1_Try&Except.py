def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

i = int(input('Введите число: '))

try:
    result = 5 * (22/i)
    print(result)
except ZeroDivisionError as exc:
    print("Нельзя делить на ноль!", exc)
else:
    print("Ура, мы не делим на ноль!!!")
finally:
    print("Наконец я закончил играться!!!")

