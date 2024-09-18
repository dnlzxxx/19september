def summa_drobei(n):
    summa = 0
    for i in range(n + 1):
        summa += 1 + i / 10
    return summa
n = int(input("Введите число N: "))
result = summa_drobei(n)
print(result)