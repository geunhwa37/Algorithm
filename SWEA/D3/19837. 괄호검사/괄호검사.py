T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    print(f'#{tc}', end=' ')

    # 괄호 검사 함수
    def stack(arr):
        stack = []

        for i in arr:
            # append
            if i in '{(':
                stack.append(i)
            # pop
            if i == '}':
                if not(stack): return 0
                if stack.pop() == '{': continue
                else: return 0
            if i == ')':
                if not (stack): return 0
                if stack.pop() == '(': continue
                else: return 0

        # 괄호가 남아있다면
        if stack: return 0

        return 1

    print(stack(arr))