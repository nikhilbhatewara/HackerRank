n, q = map(int, input().split())
lastans = 0

data = [[] for _ in range(n)]

for _ in range(q):
    a, x, y = map(int, input().split())
    i = (x ^ lastans) % n
    if a == 1:
        data[i].append(y)
    elif a == 2:
        lastans = data[i][y % len(data[i])]
        print(lastans)
