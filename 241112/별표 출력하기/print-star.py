arr = input().strip().split()
n = int(arr[0])

for j in range(n):
    for _ in range(j+1):
        print("*",end=" ")
    print()

for j in range(n-1,0,-1):
    for _ in range(j):
        print("*",end=" ")
    print()