import heapq

def main():
    n = int(input())
    sequences = []

    for _ in range(n):
        m = int(input())
        seq = list(map(int, input().split()))
        sequences.append(seq)

    heap = []
    positions = [0] * n

    for i in range(n):
        if sequences[i]:
            heapq.heappush(heap, (sequences[i][0], i))

    result = []

    while heap:
        value, seq_index = heapq.heappop(heap)
        result.append(value)

        positions[seq_index] += 1

        if positions[seq_index] < len(sequences[seq_index]):
            next_value = sequences[seq_index][positions[seq_index]]
            heapq.heappush(heap, (next_value, seq_index))

    
    print(' '.join(map(str, result)))

main()
