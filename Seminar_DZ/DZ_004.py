'''
4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.    
    Пример:    
    - 45 -> 101101
    - 3 -> 11
    - 2 -> 10
'''

n = int(input('Введите число: '))

def convert_bin(n):
    bin_num = ''
    while n > 0:
        bin_num = str(n % 2) + bin_num
        n = n // 2
    return bin_num

print(convert_bin(n))
