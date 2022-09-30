'''
3. Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.    
    Пример:    
    [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''

from random import uniform

def lst(n, first, last):
    return [round(uniform(first,last), 2) for i in range(n)]

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in (mynums)]
    return max(nums) - min(nums)

n = int(input('Введите кол-во чисел в списке: '))
first = int(input('Введите начальное значение в списке: '))
last = int(input('Введите конечное значение в списке: '))

mynums = lst(n, first, last)

print (mynums)
print(find_diff(mynums))
