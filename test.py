T = int(input())

for tc in range(1, T+1):
    # 1일 이용권의 요금, 1달 이용권의 요금, 3달 이용권의 요금, 1년 이용권의 요금
    day, mon1, mon3, year = map(int, input().split())

    plan = [0] + list(map(int, input().split())) # 12개월 이용 계획

    # 1. 전체 경우를 다보자 -> 완탐
    # 2. 각달의 최소값 -> DP

    # depth : 12 (12월을 모두 고려한 경우)
    # branch : 3개 (1일, 1달, 3달)
    def rec(month, total_cost):
        # 1일권
        rec(month + 1, total_cost + (day * plan[month]))
        # 1달권
        rec(month + 1, total_cost + mon1)
        # 3달권
        rec(month + 3, total_cost + mon3)
        # 1년권
        if month == 1:
            rec(month + 12, total_cost + (day * plan[month]))