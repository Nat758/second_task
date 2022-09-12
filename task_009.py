# Реализуйте алгоритм перемешивания списка.


# from operator import index
# from random import random


# def mix_list(list_original):
#     list= list_original[:]
#     list_length=len(list)
#     for i in range(list_length):
#         index_aleatory=random.randint(0,list_length-1)
#         temp = list[i]
#         list[i]= list[index_aleatory]=temp
#     return list
# list = [5]
# mixed_list=mix_list(list)
# print('Исходный список: ')
# print(list)
# print('Перемешанный список: ')
# print(mixed_list)

list=[1, 2, 3, 4, 5]
print(list)
import random
random.shuffle(list)
print('->',list)