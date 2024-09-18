def summa(k, n):

    summa = 0
    for i in range(k, n + 1):
        if i % 2 == 0:
            summa += i
    return summa

k = int(input("Введите начало диапазона: "))
n = int(input("Введите конец диапазона: "))

result = summa(k,n)
print(result)