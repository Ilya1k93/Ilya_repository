def main():
    try:
        q = int(input())
    except:
        q = 0

    linked_list = []
    output = []

    for _ in range(q):
        try:
            query = input().strip().split()
        except:
            query = []
        if not query:
            continue 

        if query[0] == '1':
            if len(query) != 3:
                continue
            _, x, y = query
            x = int(x)
            y = int(y)
            if x == 0:

                linked_list.insert(0, y)
            else:
                linked_list.insert(x, y)
        elif query[0] == '2':
            if len(query) != 2:
                continue
            _, x = query
            x = int(x)
            value = linked_list[x-1]
            output.append(str(value))
        elif query[0] == '3':

            if len(query) != 2:
                continue
            _, x = query
            x = int(x)
            del linked_list[x-1]

    print('\n'.join(output))

main()

