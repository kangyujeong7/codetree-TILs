first = input()
a = first.split()
second = input()
b = second.split()

A0 = int(a[0])
A1 = a[1]

B0 = int(b[0])
B1 = b[1]



if A0 >= 19 and A1 == "M":
        print(1)
elif B0 >= 19 and B1 == "M":
        print(1)
else:
    print(0)