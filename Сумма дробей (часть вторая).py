def summa_drobei(n):
    summa = 0
    for i in range(1,n + 1):
        summa += 1 / i
    return summa
n = int(input("Введите число N: "))
result = summa_drobei(n)
print(result)