def summa(k, n):

    sum = 0
    for i in range(k,n, +1):
        sum += i
    return sum

k = int(input("Введите начало диапазона: "))
n = int(input("Введите конец диапазона: "))

result = summa(k,n)
print(result)