
# from datetime import datetime
# start = datetime.now()
# nums = [num for num in range(303332)]
# # print(nums)
# finish = datetime.now()
#
#
# start2 = datetime.now()
# nums2 = []
# for i in range(303333):
#     nums2.append(i)
# # print(nums2)
# finish2 = datetime.now()
#
# print(finish - start)
# print(finish2 - start2)

# even = [num for num in range(80) if num % 2 == 0 and num % 10 == 0]
# print(even)

# my_func = lambda x,y: x+y
# print(my_func(10, 10))
#
# def add(x,y):
#     return x + y
# print(add(10, 10))


# listok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def my_func(x):
#     return x ** x
# new_listok = list(map(my_func, listok))
# print(new_listok)


# nums = [1,2,3,4,5]
# def my_func(x):
#     x  += 10
#     return x
# nums2 = list(map(my_func, nums))
# print(nums2)


# text = 'i love python'
#
# def my_func(x):
#     return x.upper()
# text2 = list(map(my_func, text))
# print(text2)
# text3 = ''.join(text2)
# print(text3)



# mixed = ['mak', 'mak', 'kopo', 'kopo', 'mak', 'kopo', 'kopo', 'mak']
# my_filter = lambda x: x == 'mak'
# zolushka = list(filter(my_filter, mixed))
# print(zolushka)


# from functools import  reduce
# nums = [x for x in range(30)]
# lambada_func = lambda x, y: x + y
# summ_all = reduce(lambada_func, nums)
# print(summ_all)




# text = 'hohhoho'
# nums = [x for x in range(20)]
# tuple_ = ('a', 'b', 'c', 'd', 'e')
# zip_func = list(zip(text, nums, tuple_))
# print(zip_func)
# tuple_ = tuple(zip(text, nums))
# print(tuple_)
# dict_ = dict(zip(text, nums))
# print(dict_)

