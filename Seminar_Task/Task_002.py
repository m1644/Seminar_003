'''
2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
'''

def func(lst):
    for item in lst:
        if isinstance(item, int) or isinstance(item, float):
            return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(func(['1982', 51, 'car', 'cow', '1234']))
