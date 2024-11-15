n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n = n % 60
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            previous = 0
            current = 1
            for i in range (n-1):
                oldprevious = previous
                previous = current
                current = (oldprevious + previous) % 10
            return current

print(fibonacci(n))
