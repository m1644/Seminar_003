'''
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.    
    Пример:    
    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]
'''

from random import randint
import math

def numbers(n, first, last):
    return [randint(first, last) for i in range(n)]

def mult_pairs(mylist):
    return [mylist[i] * mylist[-i - 1] for i in range(math.ceil(len(mylist)/2))]

n = int(input('Введите кол-во чисел в списке: '))
first = int(input('Введите начальное значение в списке: '))
last = int(input('Введите конечное значение в списке: '))

mylist = numbers(n, first, last)
print(mylist)
print(mult_pairs(mylist))
