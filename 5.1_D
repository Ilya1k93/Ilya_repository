n = int(input())

def fibonacci_sum_last_digit(n):
    if n <= 1:
        return n

    pisano_period = 60
    new_n = (n + 2) % pisano_period
    if new_n == 0:
        new_n = pisano_period

    previous = 0
    current = 1

    for _ in range(new_n - 1):
        previous, current = current, (previous + current) % 10

    result = (current - 1) % 10
    return result

print(fibonacci_sum_last_digit(n))
