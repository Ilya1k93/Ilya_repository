def main():
    try:
        n = int(input())
    except:
        print(0)
        return

    words = []
    for _ in range(n):
        word = input().strip()
        words.append(word)

    if n < 2:
        print(0)
        return

    word_length = len(words[0])
    for word in words:
        if len(word) != word_length:
            print(0)
            return

    mask_counts = {}
    for word in words:
        for i in range(word_length):
            mask = word[:i] + '*' + word[i+1:]
            if mask in mask_counts:
                mask_counts[mask] += 1
            else:
                mask_counts[mask] = 1

    total_pairs_via_masks = 0
    for mask in mask_counts:
        count = mask_counts[mask]
        if count >= 2:
            total_pairs_via_masks += count * (count -1 ) // 2

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] +=1
        else:
            word_counts[word] =1

    duplicate_pairs_total = 0
    for word in word_counts:
        count = word_counts[word]
        if count >=2:
            duplicate_pairs_total += (count * (count -1 ) //2 ) * word_length

    interesting_pairs = total_pairs_via_masks - duplicate_pairs_total

    print(interesting_pairs)

main()
