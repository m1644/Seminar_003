'''
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.    
    Пример:    
     [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

from random import randint

def lst(n, first, last):
    return [randint(first, last) for i in range(n)]

def summary(mylist):
    return sum(mylist[1::2])

n = int(input('Введите кол-во чисел в списке: '))
first = int(input('Введите начальное значение в списке: '))
last = int(input('Введите конечное значение в списке: '))

mylist = lst(n, first, last)
print(mylist)
print(summary(mylist))
