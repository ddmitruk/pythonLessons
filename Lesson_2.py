# a = 14
# print(type(a))
winter_months = ['декабрь', 'январь', 'февраль']
print(type(winter_months))  # ПРОВЕРКА ТИПА СТРОКИ
print(type(winter_months) == list)  # ПРОВЕРКА СТРОКИ, ЯВЛЯЕТСЯ ЛИ ОБЪЕКТ СПИСКОМ
print(isinstance(winter_months, list))  # ЕЩЕ СПОСОБ ПРОВЕРКИ СТРОКИ, ЯВЛЯЕТСЯ ЛИ ОБЪЕКТ СПИСКОМ
print(
    isinstance(winter_months, float))  # ЕЩЕ СПОСОБ ПРОВЕРКИ СТРОКИ, ЯВЛЯЕТСЯ ЛИ ОБЪЕКТ СПИСКОМ (на выходе получим ложь)
print(dir(winter_months))  # СПЕЦИАЛЬНАЯ ФУНКЦИЯ С ПОМОЩЬЮ КОТОРОЙ МОЖНО ПОСМОТРЕТЬ ВСЕ МЕТОДЫ
# КОТОРЫЕ СМОЖЕМ ПРИМЕНИТЬ К ДАННОМУ ТИПУ (НА СПИСОК, НА КОРТЕЖ, НА СЛОВАРЬ И Т.Д.)
# ДЛЯ СПИСКА МЕТОДЫ:
# 'append' - ДОБАВЛЯЕМ В СПИСОК ЗНАЧЕНИЕ
# 'extend' - ДОБАВЛЯЕМ В СПИСОК ЗНАЧЕНИЕ, РАСПАКОВАННОЕ ИЗ ДРУГОГО СПИСКА
# 'insert' - ДОБАВЛЯЕМ В СПИСОК ЗНАЧЕНИЕ В КОНКРЕТНОЕ МЕСТО
# 'clear',
# 'copy',
# 'count', - ПОДСЧИТЫВАЕТ КОЛИЧЕСТВО ЭЛЕМЕНТОВ
# 'index', - УЗНАЕМ ПОЗИЦИЮ (ИНДЕКС) ЗАДАННОГО ЗНАЧЕНИЯ
# 'pop' - УДАЛЯЕМ ИЗ СПИСКА ПО ИНДЕКСУ
# 'remove' - УДАЛЯЕМ ИЗ СПИСКА ПО ЗНАЧЕНИЮ
# 'reverse' - РАЗВОРАЧИВАЕМ СПИСОК БЕЗ ИЗМЕНЕНИЯ ID
# 'sort' - СОРТИРОВКА СПИСКА (НО ТОЛЬКО ОДНОТИПНЫХ ЗНАЧЕНИЙ)
my_list = [1, 3.4, 'str', False, [1, 2]]  # в списке может находиться любые значения, нет ограничений по типам
my_list.append(1)  # ДОБАВЛЯЕМ В СПИСОК ЗНАЧЕНИЕ (в самый конец)
print(my_list)
my_list.append([22, 33])  # ДОБАВЛЯЕМ В СПИСОК ЗНАЧЕНИЕ (в самый конец, можно в том числе и список)
print(my_list)
my_list.extend([22, 33])  # ДОБАВЛЯЕМ В СПИСОК ЗНАЧЕНИЕ ИЗ ДРУГОГО СПИСКА (в самый конец)
print(my_list)
my_list.insert(2, 18)  # ДОБАВЛЯЕМ В СПИСОК ЗНАЧЕНИЕ В КОНКРЕТНОЕ МЕСТО (сначало место, потом значение)
print(my_list)
print(my_list.index(1))  # УЗНАЕМ ПОЗИЦИЮ (ИНДЕКС) ЗАДАННОГО ЗНАЧЕНИЯ, даст ответ первого индекса, которое встретит
print(my_list.index(False))
print(my_list.count(1))  # ПОДСЧИТЫВАЕТ КОЛИЧЕСТВО ЭЛЕМЕНТОВ
print(my_list.count(77))  # ПОДСЧИТЫВАЕТ КОЛИЧЕСТВО ЭЛЕМЕНТОВ, если значения нет в списке - вернет значение 0
my_list.remove(1)  # УДАЛЯЕМ ИЗ СПИСКА ПО ЗНАЧЕНИЮ, удалит значение первого индекса, которое встретит
print(my_list)
my_list.pop(6)  # УДАЛЯЕМ ИЗ СПИСКА ПО ИНДЕКСУ, если не указывать индекс, то удалит последний
print(my_list)
my_list[-4].pop(1)  # УДАЛЯЕМ ИЗ СПИСКА В СПИСКЕ ПО ИНДЕКСУ
print(my_list)
a = my_list.pop()  # УДАЛЯЕМ ИЗ СПИСКА ПО ИНДЕКСУ, и присваиваем его в переменную
print(a)
print(my_list)
print(id(my_list))  # проверка id списка
my_list.reverse()  # РАЗВОРАЧИВАЕМ СПИСОК БЕЗ ИЗМЕНЕНИЯ ID
print(my_list)
print(id(my_list))  # проверка id списка
my_list.reverse()  # РАЗВОРАЧИВАЕМ ОБРАТНО СПИСОК БЕЗ ИЗМЕНЕНИЯ ID
print(my_list)
n = list(reversed(my_list))  # РАЗВОРАЧИВАЕМ СПИСОК И СОЗДАЕМ НОВЫЙ С ИЗМЕНЕНИЕМ ID
print(n)
print(id(n))
# my_list.sort()  # СОРТИРОВКА СПИСКА, т.к. нельзя сортировать разнотипные значения
# print(my_list)

winter_months = ['декабрь', '45', 'январь', '$', 'февраль', '6']
print(winter_months)
print(id(winter_months))
winter_months.sort()  # СОРТИРОВКА СПИСКА
print(winter_months)
print(id(winter_months))
print(ord('$'))  # прверка номера символа в языке
print(ord('4'))
print(ord('6'))
print(ord('д'))
print(ord('ф'))
nn = sorted(winter_months, reverse=True)  # создать новый объект, с разворотом объекта (в данному случае от большего к меньшему)
print(nn)
# m = sorted(my_list, reverse=True) # выдаст снова ошибку, т.к. невозможно отсортировать разнотипные значения

tuple('dfgsvbe')  # создание кортежа
print(tuple('dfgsvbe'))
k = (1, 2, 3)  # тоже создание кортежа
print(type(k))
k = 1, 2, 3, 5, 7  # тоже создание кортежа (главное чтобы была запятая)
print(type(k))
k = 1,  # тоже создание кортежа (главное чтобы была запятая)
print(type(k))
my_tuple = (1, 3.4, 'str', False, [1, 2])
print(type(my_tuple))
print(my_tuple[0])  # кортеж работает с индексами
print(my_tuple[2:])  # кортеж работает со срезами
# my_tuple[0] = 11 # выдаст ошибку, т.к. нельзя в кортеже менять значения

import sys  # проверка размера списка и кортежа (кортеж всегда легче)

some_list = ['hello', True, 'word', 1, 2.2]
print(sys.getsizeof(some_list))
some_tuple = ('hello', True, 'word', 1, 2.2)
print(sys.getsizeof(some_tuple))

print(dir(my_tuple))
# ДЛЯ КОРТЕЖА МЕТОДЫ ТОЛЬКО:
# 'count' - УЗНАТЬ КОЛИЧЕСТВО ПОВТОРЕНИЙ В КОРТЕЖЕ
# 'index' - УЗНАТЬ ИНДЕКС ЭЛЕМЕНТА В КОРТЕЖЕ
print(my_tuple)
my_tuple[-1].append(3)  # если в кортеже есть список то можно в списке использовать все методы для списка)
print(my_tuple)

n = [1, 2]
m = n
print(n)
print(m)
n.append(3)
print(n)
print(m)  # m в таком случае всегда будет равен n
m = n[:]
n.append(4)
print(n)
print(m)  # m в таком случае не будет равен n и с переменной n можго все делать
m = n.copy()
n.append(5)
print(n)
print(m)  # m и в таком случае не будет равен n и с переменной n можго все делать

n = [1, 2, [11, 22]]
m = n.copy()
n[-1].append(33)
print(n)
print(m)  # не учитывает вложенные значения, т.е. поверхностное копирование

from copy import deepcopy

m = deepcopy(n)
n[-1].append(44)
print(n)
print(m)

name, age = 'Ivan', 23  # количество значений слева должен быть равен количеству значений справа
print(name)
print(age)
# name, *age = 'Ivan', 23, 78 # если добавить*, то age станет списком
# print(name)
# print(age)
print('Your name', name, 'and age', age, '.')
print('Your name %s and age %d.' % (name, age))
print('Your name {} and age {}.'.format(name, age))
print('Your name {} and age {}.'.format(age, name))
print('Your name {1} and age {0}.'.format(age, name))
print(f'Your name {name} and age {age}.')
print(f'{100 / 7}')
print(f'{100 / 7:.3f}')  # округляем
print(f'{100 / 7:.2f}')
print(f'{7}')
print(f'{7:02}')  # дополняем нулями перед числом (должно получиться 2 числа
print(f'{7:03}')
print(f'{7:4}')  # дополняет пробелами
print(f'{7:4}')

print('-' * 10)

r = str([1, 2, 3])  # преобразование в строку, в которой поддерживается индексация, слайсы
print(r[0])
print(dir(r))
r = '1 2 3 4'.split() # разделение строки
print(r)
print(type(r))
r = ' '.join(['Name', 'Surname']) # склеивание строки
print(r)
r = ' & '.join(['Name', 'Surname'])
print(r)

l = 'СссР'.lower() # приведение к нижнему регистру
print(l)
l = 'СссР'.upper() # приведение к верхнему регистру
print(l)
l = 'сЕрГеЙ сЕрГеЙ сЕрГеЙ'.title() # приведение к заглавной букве каждого слова в строке
print(l)
l = 'сЕрГеЙ сЕрГеЙ сЕрГеЙ'.capitalize() # приведение к заглавной букве только первого слова в строке
print(l)

j = 'gippopopotamus'.count('po') # поиск количества символов
print(j)
j = 'gippopopotamus'.replace('po', 'pa') # замена символа в списке
print(j)
j = 'gipopopotamus'.find('po') # поиск символа в списке (выводит индекс первого вхождения)(если нет - выводит -1)
print(j)
j = 'gipopopotamus'.find('po', 5) # поиск символа в списке с указанием с какого места (выводит индекс первого вхождения)
print(j)
j = 'gipopopotamus'.index('t') # поиск символа в списке (выводит индекс первого вхождения)(если нет - выводит ошибку)
print(j)

h = '123456'.isdigit() # проверяет, является ли значение целочисленным. Не работает с буквами, отрицательными числами и дробными)
print(h)
h = '12345.6'.replace('.', '').isdigit() # в случае необходимости работы с дробными числами
print(h)

a = 15 * 3
print(type(a))