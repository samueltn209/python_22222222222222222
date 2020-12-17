# new_list = []
# empty_list = list()
# list_ = [1, 2, 3, 4, 5, 6]
# print(len(list_))
# print(list_)
#
#
#
#
# diapazon = range(1, 21)
# print(list(diapazon))


# method append добавляет элементы в конец списка

# some_list = [1, 2, 3, 4, 5]
# print(some_list)
# some_list.append(6)
# print(some_list)
# some_list.append('python')
# print(some_list)
# print(len(some_list))
# new_list = [1,2,3]
# some_list.append(new_list)
# print(some_list)


# method extend расширяет список другим списком

# list1 = ['user1', 'user2', 'user3']
# list2 = ['tim', 'bul','amir']
# list3= ['tom', 'mike', 'kim']
# list2 += list3
# list4 = list1 + list2
# list1.extend(list2)
# print(list1)
# print(list1)
#

# # method insert  получает 2 агргумента м добавляет в список поиндексно

# cars = ['subaru', 'honda', 'bmw']
# print(cars)
# cars.insert(3, 'toyota')
# print(cars)


# method remove удаляет элемент по значению

# laptops = ['lenovo', 'macbook', 'acer', 'asus']
# laptops.remove('asus')
# print(laptops)


# method pop удаляет последний по умолчанию элемент но можно передать индекс удаляемого элемента

# laptops = ['lenovo', 'macbook', 'acer', 'asus']
# notebook = laptops.pop(2)
# last_notebook = laptops.pop()
# print(notebook)
# print(laptops)
# print(last_notebook)



# method index возвращает индекс элемента

# laptops = ['lenovo', 'macbook', 'acer', 'asus']
# print(laptops.index('asus'))


# method count

# numders = [1, 2, 1, 3, 2, 1, 2, 3, 1]
# print(numders.count(2))


# method reverse разворачивает список

# numders = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numders.reverse()
# print(numders)


# method  sort  сортирует по ключу

# nums = [1, 5, 4, 3, 6, 7]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# laptops = ['lenovo', 'macbook', 'acer', 'asus']
# laptops.sort(key=len, reverse=True)
# print(laptops)

# method copy копируте лист

# cars = ['subaru', 'honda', 'bmw']
# print(cars)
# new_cars = cars.copy()
# new_cars[2][0] = 'gaz'
# print(new_cars)


# method deepcopy

# import copy
# list_ = [1, 2, 3, [4, 5, 6]]
# print('original', list_)
# new_list = copy.deepcopy(list_)
# print('copy', new_list)
# new_list[3][0] = 'changed'
# print('copy', new_list)
# print('orginal', list_)



# method clear  полностью очищает список
# method del  полностью удаляет элемент

# cars = ['subaru', 'honda', 'bmw']
# # cars.clear()
# del cars[1]
# print(cars)


# # import math
# from datetime import datetime
# print(datetime.now())

# срезы

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_[0:5])
# print(list_[1::3])


# кортежи - tuples

# new_tuple = ('abc',)
# print(type(new_tuple))
# tuple_ = tuple()
# print(type(tuple_))
# print(dir(tuple_))

# numders = (1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 3, (1, [1,2]))
# print(numders.index(3))
# print(numders.count(3))
#
# numbers = list(numders)
# print(numders)
# numbers.clear()
# numbers = tuple(numbers)
# print(numbers)

