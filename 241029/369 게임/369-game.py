n = int(input().strip())

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end=" ")
    else:
        i_str = str(i)
        if any(digit in '369' for digit in i_str):
            print(0, end=" ")
        else:
            print(i, end=" ")