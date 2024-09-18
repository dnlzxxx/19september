def summa_drobei(n):
    summa = 0
    for i in range(1, n + 1):
        summa += 1 + (z ** i)
    return summa
n = int(input("Введите число N: "))
z = int(input("Введите значение: 1"))
result = summa_drobei(n)
print(result)