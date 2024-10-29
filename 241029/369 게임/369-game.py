n = int(input().strip())

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end=" ")
    else:
        i_str = str(i)  # 숫자를 문자열로 변환
        t = len(i_str)  # 문자열의 길이를 통해 자릿수 확인

        if t == 2:  # 두 자릿수인 경우
            if i_str[0] == '3' or i_str[0] == '6' or i_str[0] == '9':
                print(0, end=" ")
            elif i_str[1] == '3' or i_str[1] == '6' or i_str[1] == '9':
                print(0, end=" ")
            else:
                print(i, end=" ")
        else:  # 한 자릿수인 경우
            if i_str == '3' or i_str == '6' or i_str == '9':
                print(0, end=" ")
            else:
                print(i, end=" ")