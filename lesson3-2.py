# dictionary - словарь
# new_dict = {}
# new_dict2 = dict()
# print(new_dict)
# print(new_dict2)
# print(dir(new_dict))
#
# new_dict = {'key': 'value', 'key2':'value2', ' tim': '505878999'}
# print(new_dict)

# capitals = {}
# capitals['kg'] = 'bsh'
# capitals['ru'] = 'msk'
# print(capitals)


# capitals = dict(russia='moscow', kyrgozstan='bishkek', usa='washington' )
# print(capitals)

# capitals = dict([('russia','moscow'), ('kyrgozstan','bishkek'), ('usa','washington' )])
# print(capitals)
#
# new_dict = dict(zip(['russia', 'kyrgizsistan', 'usa'], ['moscow', 'bishkek', 'washigton']))
# print(new_dict)


# method fromkeys  создает словарь из ключей

# dictionary = dict.fromkeys(['ket1', 'key2'], 'какое-то значение')
# print(dictionary)
#
#
# # method get  получает по ключу значение
#
# capitals = dict(russia='moscow', kyrgozstan='bishkek', usa='washington' )
# print(capitals.get('russia'))
#
# numbers = {1: 2, 3: 4, 5: 6}
# print(numbers[1])
# numbers[7] = 8
# print(numbers)
# numbers[3] = 22222
# print(numbers)


# method kays выводит все клюи из словаря
# method values выводит все значения
# method items возвращает пару ключ и знаечение
# method pop удаляет по ключу и возвращает значение
# capitals = dict(russia='moscow', kyrgozstan='bishkek', usa='washington' )
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# Russia = capitals.pop('russia')
# print(Russia)
# print(capitals)


# method update обновляет словарь (складывает словари)

# capitals = dict(russia='moscow', kyrgozstan='bishkek', usa='washington' )
# capitals2 = {'belarus': 'minsk', 'russia': 'valdivostok'}
# capitals.update(capitals2)
# print(capitals)


# method popitem не принимает аргументы удаляет последний элемент

# capitals = dict(russia='moscow', kyrgozstan='bishkek', usa='washington' )
# usa = capitals.popitem()
# print(capitals)
# print(usa)


# method setdefault
# capitals = dict(russia='moscow', kyrgizstan='bishkek', usa='washington' )
# new = capitals.setdefault('кыргызстан')
# print(new)
# print(capitals)
