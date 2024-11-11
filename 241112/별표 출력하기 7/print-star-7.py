arr = input().strip().split()
n= int(arr[0])

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()