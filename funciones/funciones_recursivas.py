# 1, 1, 2, 3, 5, 8, 13, 21, ...
def fibo_iterativo(n):
    if n <= 2:
        return 1
    else:
        t1 = 1
        t2 = 1
        contador = 3
        while contador <= n:
            t1, t2 = t2, t1 + t2
            contador += 1
        return t2
    
def fibo_recursivo(n):
    if n <= 2:
        return 1
    else:
        return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)

print(fibo_iterativo(9))
print(fibo_recursivo(9))
