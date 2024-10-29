n = int(input().strip())





for i in range(1,n+1):
    if i%3 == 0: 
        print(0,end=" ")
    else:
        i_str = str(i)                
        k =  i_str.split()
        t = len(k)

        if t == 2 :
            if k[0] == '3'or'6' or '9':
                 print(0,end=" ")
            elif k[1] == '3'or'6' or '9':
                 print(0,end=" ")
        else:
            print(i,end=" ")