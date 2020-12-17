# set
# new_set = {9,2,3,4,1,6,7,8}
# print(new_set)
# # new_list = [1,2,3,4,5,3,2,1,1,3]
# # print(new_list)
# # new_list = set(new_list)
# # print(new_list)
#
#
# set_ = {}
# print(type(set_))
# print(type(new_set))
# print(len(new_set))


# method add Принимает один аргумент который может быть любого типа и добавляет данное значение в множество
# method update принимает один аргумент - iterable и добавляет все его элементы к исходному множеству

# a_set = {1, 2, 0, ('sad', 'bad')}
# a_set.add(4)
# print(a_set)
# a_set.add('4')
# print(a_set)
# list_ = [2,3,4,5,6,7,8,9]
# b_set = {9, 4, 5, 6}
# a_set.update(list_)
# print(a_set)
#
#
# # method remove удаляет значение
#
# a_set.remove(1)
# print(a_set)
#
# # method discard
#
# a_set.discard(2)
# a_set.remove(0)
# print(a_set)
#
# # method pop method clear
#
# print(a_set.pop())
# a_set.clear()
# print(a_set)

# method union (обьединение) возвращает новое множество множества

# a_set = {2, 4, 5, 9, 12, 22, 31, 55, 78, 130, 199}
# b_set = {3, 4, 65, 23, 41, 54, 43, 15, 123, 321, 146}
# a_set.union(b_set)
# print(a_set)

# set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set_2 = {1, 3, 6, 9}
# print(set_2.union(set_1))

# method instersection (пересечение) возвращает новое множество содержащее все элементы которые есть и  в первом множестве и во вотором

# set_1 = {1,2,3,4,5,6,7,8,9}
# set_2 = {2,4,6,7,8,33,11,123}
# set_3 = set_1.intersection(set_2)
# print(set_3)


# method difference (разность)  возвращает новое множество содержащее все элементы которые есть в множетсве a_set  но которыех нет в множестве  b_set

# set_1 = {1,2,3,4,5,6,7,8,9}
# set_2 = {2,4,6,7,8,33,11,123}
# print(set_1.union(set_2)) #сложение
# print(set_1.intersection(set_2)) #пересечение
# print(set_1.difference(set_2)) #разность
# print(set_1.symmetric_difference(set_2)) #симетричная разность

# mthod symmetrick_difference (симетрическая разность) возвращает нвове множество которое содержит только уникальные элементы обоих множеств




# boolean

# x = True
# y = False
#
# if 1 < 0:
#     print(type(True))
#
#
# elif 2 < 0:
#     print(True)
#
# else:
#     print('сработал блок else')



# ==    СРАВНЕНИЕ
# !=    ОТРИЦАНИЕ
# <     МЕНЬШЕ
# >     БОЛЬШЕ
# <=    МЕНЬШЕ РАВНО
# >=    БОЛЬШЕ РАВНО
# and   И
# or    ИЛИ
# not   НЕ

# point = input('Enter your point:')
# if point == '5':
#     print('молодец')
# elif point == '4':
#     print("ты молодец чуть чуть осталось до отличника")
# elif point == "3":
#     print("старайся учиться лучше!")
# else:
#     print("неудачник")



# list_ = [1, 2, 3, 4, 5]
# num = int(input(' enter a number:'))
# if num  in list_:
#     print('есть такое число')
# else:
#     print('такого нету')
#
# list_ = [1, 2, 3, 4, 5]
# num = int(input(' enter a number:'))
# if num not in list_:
#     print('такого нету')
# else:
#     print('есть такое число')

# number1 = int(input('enter a number1: '))
# number2 = int(input('enter a number2: '))
# if number2 > 5 and number2 > 10:
#     print(number1 - number2)
# elif number1 > 5 or number2 > 10:
#     print(number1 + number2)


# while True:
#     number1 = int(input('enter a number1: '))
#     number2 = int(input('enter a number2: '))
#     operator = input('enter a operator +-*/: ')
#     if operator == '+':
#         print(number1 + number2)
#     elif operator == '-':
#         print(number1 - number2)
#     elif operator == '*':
#         print(number1 * number2)
#     elif operator == '/':
#         print(number1 / number2)
#     else:
#         print('введите оператор +-*/')


# import math
# while True:
#     number1 = float(input('enter a number1: '))
#     number2 = float(input('enter a number2: '))
#     number3 = float(input('enter a number3: '))
#     operator = input('enter a operator +-*/: ')
#     if operator == '+':
#         print(math.floor(number1 + number2 + number3))
#         print(number1 + number2 + number3)
#     elif operator == '-':
#         print(number1 - number2)
#     elif operator == '*':
#         print(number1 * number2)
#     elif operator == '/':
#         print(number1 / number2)
#     elif operator.isalpha()
#         print('вы остановили цикл')
#         break
#     else:
#         print('введите оператор +-*/')



