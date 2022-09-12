# Задайте список из n чисел последовательности
#  $(1+\frac 1 n)^n$ и выведите на экран их сумму.

from unittest import result


n=int(input('Ведите число n для $(1+\frac 1 n)^n$ : '))
result_list = list((1+1/i)**i for i in range(1, n+1))
print(f'sum for 3 = {round(sum(result_list),3)}')