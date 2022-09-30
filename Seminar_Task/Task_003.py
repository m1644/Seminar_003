'''
3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
'''

def func(string):
    lst = ['qwe', 123, '123', '234', 'qwe', '234']
    count = 0
    for i in range(len(lst)):
        if lst[i] == string:
            count += 1

        if count == 2:
            return i
    return - 1

if __name__ == '__main__':
    print(func(input('Введите строку для поиска: ')))
