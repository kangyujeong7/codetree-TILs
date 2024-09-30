n = int(input())
arr = list(map(float,input().strip().split()))

sum_val = 0
for i in range(len(arr)):
    sum_val += arr[i] 
K =round(sum_val/n,1)

print(K)

if K >=4.0:
    print("Perfect")
elif K >=3.0:
    print("Good")
else:
    print("Poor")