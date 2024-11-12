arr = input().strip().split()

n = int(arr[0])

for j in range(n):
    for _ in range(n-j,0,-1):
        print("*",end=" ")
    print()
for i in range(n):
    for _ in range(i+1):
        print("*",end=" ")
    print()
