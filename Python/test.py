def fibonacci_list(n):
    fib = [1, 1]
    if n == 1:
        fib = [1]
    else:
        for k in range(2, n):
            fib.append(fib[k-1]+fib[k-2])
    return fib

pro = fibonacci_list(10)
print(pro)

print(100//5, 20/4, 9/3)

print(len(pro))