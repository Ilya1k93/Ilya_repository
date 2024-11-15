def factorial(n):
    f = n
    for i in range(1,n):
        f = f*i
    return f

input1 = int(input())
print(factorial(input1))
