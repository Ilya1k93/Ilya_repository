n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    else:
        previous = 0
        current = 1
        for i in range (n-1):
            oldprevious = previous
            previous = current
            current = oldprevious + previous
        return current

print(fibonacci(n))
