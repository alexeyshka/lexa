from math import sqrt

print("Задача 1")

arr = [x for x in range(5, 101, 5)] # создание списка с помощью объекта генератора
print("Список:", arr)

print("\nЗадача 2")

tpl = tuple(arr) # создание кортежа с помощью явного преобразования
print("Кортеж:", tpl)

arr.clear() # очистка списка
print("Очищенный список:", arr)

print("\nЗадача 3")

dct = {}
n = int(input("Количество элементов словаря: "))
for i in range(n):
    a, b = map(int, input().split())
    dct[a] = b

dct = dict(sorted(dct.items(), key = lambda x: x[1])) # сортировка словаря по ключу с лямбда-функцией
print("Ключи отсортированного словаря: ", ', '.join(map(str, dct.keys()))) # вывод списка ключей в строку через разделитель ', '

print("\nЗадача 4")

# arr = list(map(lambda x: x+39 if x >= 50 else x*3, tpl))
arr.extend(list(map(lambda x: x+39 if x >= 50 else x*3, tpl)))
print(arr)

for x in tpl:
    arr.append(x)
print(arr)

print("\nЗадача 5")

def func1(line):
    arr_line = list(filter(lambda x: 'A' <= x[0] <= 'Z', line.split()))
    return sorted(arr_line)

text = str(input("Строка: "))
print("Отсортированный список: ", func1(text))

print("\nЗадача 6")

def func2(dict):
    l_max = max(dict.keys(), key = len) # определение ключа с максимальной длиной
    l_min = min(list(dict.keys()), key = len)
    v_max = dict[l_max] # значение, соответствующее ключу с максимальной длиной
    v_min = dict[l_min]
    return v_max, v_min

dct2 = {}
n = int(input("Количество элементов словаря: "))
for i in range(n):
    a, b = input().split()
    dct2[a] = int(b)

val_max, val_min = func2(dct2)
print(f"Значение с самым длинным ключом: {val_max}\nЗначение с самым коротким ключом: {val_min}")

val_m = (val_max + val_min)/2
dct2 = dict(filter(lambda x: len(x[0]) < val_m, dct2.items()))

print(dct2)

print("\nЗадача 7")

# функция-предикат, определяющая простое ли число
def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0: return False
    return True

def func3(num):
    ar = []
    for i in range(2, num):
        if is_prime(i): ar.append(i)
    return ar

val = int(input("Введите число: "))
arr_prime = func3(val)

if arr_prime:
    print(f"Простые числа, меньшие {val}: {arr_prime}")
else:
    print(f"Простых чисел, меньших {val} нет")

