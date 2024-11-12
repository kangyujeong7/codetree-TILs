arr = input().strip().split()
n = int(arr[0])

for i in range(n):
    for _ in range(i+1):
        print("*",end="")
    print()
    print()

for j in range(n):
    for _ in range(n-j,0,-1):
            print("*",end="")
    print()
    print()