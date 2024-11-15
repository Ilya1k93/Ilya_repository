m, n = map(int, input().split())

def fibonacci_sum_last_digit(m, n):
    if m > n:
        m, n = n, m

    pisano_period = 60

    def get_fibonacci_huge(n):
        n = n % pisano_period
        if n <= 1:
            return n

        previous = 0
        current = 1

        for _ in range(n - 1):
            previous, current = current, (previous + current) % 10
        return current

    sum_n = get_fibonacci_huge(n + 2)
    sum_m = get_fibonacci_huge(m + 1)

    result = (sum_n - sum_m) % 10
    return result

print(fibonacci_sum_last_digit(m, n))
