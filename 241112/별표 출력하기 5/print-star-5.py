arr = input().strip().split()
n = int(arr[0])

for i in range(n,0,-1): 
    for j in range(i):
        print("*"*i,end=" ")
    print()