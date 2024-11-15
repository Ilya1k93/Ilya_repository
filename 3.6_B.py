n = int(input())
a = list(map(int, input().split()))

def quicksort_iterative(a):
    size = len(a)
    stack = []

    stack.append(0)
    stack.append(size - 1)

    while stack:
        right = stack.pop()
        left = stack.pop()

        if left >= right:
            continue

        pivot_index = left + (right - left) // 2
        pivot = a[pivot_index]

        a[pivot_index], a[right] = a[right], a[pivot_index]

        partition_index = left
        for i in range(left, right):
            if a[i] < pivot:
                a[i], a[partition_index] = a[partition_index], a[i]
                partition_index += 1

        a[partition_index], a[right] = a[right], a[partition_index]

        if partition_index - left > right - partition_index:
            stack.append(left)
            stack.append(partition_index - 1)
            stack.append(partition_index + 1)
            stack.append(right)
        else:
            stack.append(partition_index + 1)
            stack.append(right)
            stack.append(left)
            stack.append(partition_index - 1)

quicksort_iterative(a)
print(' '.join(map(str, a)))
