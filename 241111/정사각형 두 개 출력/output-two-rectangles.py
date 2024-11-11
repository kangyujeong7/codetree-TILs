arr = input().strip().split()

n = int (arr[0])

for _ in range(2):
    for _ in range(n):
        for _ in range(n):
            print('*',end="")
        print()
    print()