T = int(input())

for tc in range(1, T+1):
    arr = list(input().split())

    print(f'#{tc}', end=' ')

    stack = []

    for i in arr:
        # 숫자인 경우 append
        if i.isdigit():
            stack.append(i)
        # 연산자인 경우
        else:
            # 출력
            if i == '.':
                if len(stack) == 1:
                    print(int(stack.pop()))
                else:
                    print('error')
                break

            # 형식이 잘못되어 연산이 불가능한 경우
            if len(stack) < 2:
                print('error')
                break

            # 계산
            a = int(stack.pop())
            b = int(stack.pop())

            if i == '+':
                stack.append(b+a)
            elif i == '-':
                stack.append(b-a)
            elif i == '*':
                stack.append(b*a)
            elif i == '/':
                stack.append(b//a)
