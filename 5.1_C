n, m = map(int, input().split())

def PisanoPeriod(m):
    current = 0
    next = 1
    period = 0
    while True:
        oldNext = next
        next = (current + next) % m
        current = oldNext
        period = period + 1
        if current == 0 and next == 1:
            return period

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        mod = PisanoPeriod(m)
        n = n % mod
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
                current = (oldprevious + previous) % m
                n_mod = current % m
            return n_mod

print(fibonacci(n))
