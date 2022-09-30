'''
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.    
    Пример:    
 для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
 [Негафибоначчи](https://ru.wikipedia.org/wiki/Негафибоначчи)
'''

k = int(input('Введите число k: '))

negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,k):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f'Для числа k = {k} список чисел Фибоначи - {negofibonacci+fibonacci}')
