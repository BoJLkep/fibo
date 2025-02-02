def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Пример использования
n = 10
print(f"Число Фибоначчи под индексом {n} равно {fibonacci(n)}")
