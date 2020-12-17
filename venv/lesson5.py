# method replace  меняет старое значение на новое

# text = "I love Java"
# print(text.replace('Java', 'Python'))

# x = 0
# for i in range(20):
#     x += 1
#     print('pppp', x)

# import time
#
#
# numbers = []

# for number in range(40):
#     numbers.append(number)
#     # print(number)
#     time.sleep(0.5)
#     print(numbers)

#                                                      range(начало, конец, шаг)

# text = 'privet'
# for i in text:
#     print(i.upper())

# for i in range(66):
#     if i % 2 == 0 and i % 5 == 0:
#         print(i)



# i = 0
# while i <= 10:
#     print('fu')
#     i += 1


# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 10:
#         break

# total = 100
# i = 0
# while i < 5:
#     n = int(input('input number'))
#     total -= n
#     i += 1
# print('осталось', total)

# i = 0
# while i < 20:
#     print('тестовая строка')
#     i = i + 1
#     if i == 10:
#         print('continue')
#         continue
#     print('continue  не сработала')
#     if i == 18:
#         print('break')
#         break


# def is_palindrome():
#     text = 'tenet'
#     if text == text[::-1]:
#         print('its palindrom')
#     else:
#         print('itss not polindrom')
# is_palindrome()



# def hello():
#     print('hello')
#
# hello()



# name = input('input your name: ')
# def hello(name):
#     print(f"hello, {name}")
# hello(name)


# def add(x, y):
#     print(x + y)
#
# add(10,10)



# def add(x, y):
#     return x + y
#
# print(add(20, 40))





                                                                        # word = input()
                                                                        # print(word[::-1])




# name = 'tom'
#
# def my_func():
#     print(name)
#
# my_func()

# def my_func():
#     name = 'tom'
#     print('принт из функции' + name)
#
# my_func()
# print(name)



# def my_func(x, y):
#     z = x ** y
#     return z
# var = my_func(3,3)
# print(var)


# num = 1234
# def my_func():
#     num = 123
#     print(num)
# my_func()
# print(num)


# def add(q,w,e,r,t,y,u,i,o,p):
#     return q + w + e + r + t + y + u + i + o + p
# print(add(1, 2 ,3 , 4, 5, 6, 7, 8, 9, 0))
#
# def add2(*args):
#     resultat = 0
#     obj = args
#     for i in args:
#         resultat = resultat + 1
#     return resultat
# nums = (1,2,3,4,2,1,2,3,4,1,2,3,1)
# print(add2(nums))
#


#
# def my_func(x,y,z=20):
#     return x + y + z
# print(my_func(1,2,3))
# var = 'hello'
# print(var, var, sep='____')



#
# def my_func(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key} is {value}")
#
# my_func(a=1,b=2,c=3 )


# import time
# def recursive_func():
#     print('У попа была собака он  её любил')
#     print("она съела косук мяса, он её убил")
#     print("в землю закопал и надпись написал")
#     time.sleep(0.2)
#     recursive_func()
# recursive_func()