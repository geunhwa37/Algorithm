24352. 경비원의 감시
[링크](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZvefmuKBurHBIN6&contestProbId=AZZRsBy6QBjHBIMK&probBoxId=AZwb8CG6bUnHBIT3&type=USER&problemBoxTitle=im+%EA%B8%B0%EC%B6%9C+%EB%AC%B8%EC%A0%9C&problemBoxCnt=4&&&&&&)

문제 내용

시간 : 10개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 1초 / Python의 경우 3초
메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

N x N 크기의 격자 모양 건물이 있습니다. 이 건물의 각 칸은 빈 공간(0), 벽(1), 또는 경비원(2)으로 채워져 있습니다.

경비원은 정확히 1명만 존재하며, 자신이 있는 칸에서 상, 하, 좌, 우 네 방향으로 벽을 만나기 전까지 모든 칸을 감시할 수 있습니다.

당신의 임무는 이 단일 경비원이 감시하지 못하는 칸의 개수를 찾는 것입니다.


[입력]

첫 줄에 테스트 케이스의 개수 T가 주어집니다.

각 테스트 케이스의 첫 줄에는 건물의 크기 N이 주어집니다.

다음 N줄에 걸쳐 각 줄마다 N개의 숫자가 공백으로 구분되어 주어집니다.

0은 빈 공간, 1은 벽, 2는 경비원을 나타냅니다.


[출력]

각 테스트 케이스마다 '#x'(x는 테스트케이스 번호)를 출력하고, 공백을 둔 다음 경비원이 감시하지 못하는 칸의 개수를 출력합니다.


[제약사항]

1 ≤ N ≤ 100

벽은 1개 이상 존재할 수 있습니다.

경비원은 정확히 1명만 존재합니다.
