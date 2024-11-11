arr = input().strip().split()

n = int(arr[0])


for i in range(1,n+1):
    d=1+2*(i-1)
    for j in range(d):
        print("*",end="")
    print()