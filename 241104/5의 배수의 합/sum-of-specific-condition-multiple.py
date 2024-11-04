arr = input().strip().split()

#arr = list(map(int,k)) #문자열이 붙어 있으면 그냥 k[0],k[1] 이렇게 바로 접근하면 되지만, 그렇지 않을수도 있다. 아근데 list로 감싸면 int없어지니깐 의미 x

a,b = int(arr[0]) , int(arr[1])


_sum=0

if a < b:
    for i in range(a,b+1):
        if i % 5 == 0:
            _sum+=i
else:
     for i in range(a,b+1):
        if i % 5 == 0:
            _sum+=i

print(_sum)