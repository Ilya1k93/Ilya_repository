n = int(input().strip())
a = list(map(int, input().split()))

head = None

for i in reversed(range(n)):
    if head is None:
        node = (a[i], i, float('inf'), None, float('-inf'), None, None)
    else:
        value, index, min_right_value, min_right_index, max_right_value, max_right_index, next_node = head
        if value < min_right_value or (value == min_right_value and index < min_right_index):
            current_min_value = value
            current_min_index = index
        else:
            current_min_value = min_right_value
            current_min_index = min_right_index
        if value > max_right_value or (value == max_right_value and index < max_right_index):
            current_max_value = value
            current_max_index = index
        else:
            current_max_value = max_right_value
            current_max_index = max_right_index
        node = (
            a[i],
            i,
            current_min_value,
            current_min_index,
            current_max_value,
            current_max_index,
            head
        )
    head = node

min_diff = float('inf')
min_pair = (None, None)
max_diff = float('-inf')
max_pair = (None, None)

current = head
while current is not None:
    value, index, min_right_value, min_right_index, max_right_value, max_right_index, next_node = current
    if max_right_index is not None and index < max_right_index:
        diff_min = value - max_right_value
        if diff_min < min_diff:
            min_diff = diff_min
            min_pair = (index, max_right_index)
        elif diff_min == min_diff:
            if index < min_pair[0] or (index == min_pair[0] and max_right_index < min_pair[1]):
                min_pair = (index, max_right_index)
    if min_right_index is not None and index < min_right_index:
        diff_max = value - min_right_value
        if diff_max > max_diff:
            max_diff = diff_max
            max_pair = (index, min_right_index)
        elif diff_max == max_diff:
            if index < max_pair[0] or (index == max_pair[0] and min_right_index < max_pair[1]):
                max_pair = (index, min_right_index)
    current = next_node

i_1, j_1 = min_pair
i_2, j_2 = max_pair

print(i_1 + 1, j_1 + 1)
print(i_2 + 1, j_2 + 1)
