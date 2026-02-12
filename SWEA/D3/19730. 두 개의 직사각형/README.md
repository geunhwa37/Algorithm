19730. 두 개의 직사각형
[링크](https://swexpertacademy.com/main/talk/solvingClub/problemPassedUser.do?contestProbId=AY1n3tPaWcEDFAWX&solveclubId=AZvefmuKBurHBIN6&problemBoxTitle=im+%EA%B8%B0%EC%B6%9C+%EB%AC%B8%EC%A0%9C&problemBoxCnt=8&probBoxId=AZwb8CG6bUnHBIT3)

문제 내용

시간 : 5개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 1초 / Python의 경우 3초

메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

펜을 사용할 수 있는 스마트폰은 Air View 기능이 있다.

이것은 펜이 스마트폰 표면에 닿기 직전의 상황에서 다양한 조작을 해주는 기능이다.

Air View는 직사각형(정사각형 포함) 모양으로만 존재하며,

화면에 2개의 Air View가 있을 때, 두 Air View는 아래 4개의 상태 중 1개에 속한다.


①번 상태 : Air View 사이에 겹치는 영역이 존재한다.




②번 상태 : 1번에 해당하지 않으며, 겹치는 선이 존재한다.




③번 상태 : 1, 2번에 해당하지 않으며, 겹치는 점이 존재한다.




④번 상태 : 1, 2, 3번에 해당하지 않는다.



 

두 개의 Air View 좌표가 주어질 때, 두 Air View가 몇 번 상태에 속하는지 출력하라!

좌표는 다음과 같이 (x1, y1), (x2, y2)로 주어진다.

 


[제약 사항]

1. Air View는 직사각형(정사각형 포함) 모양으로 주어진다.

2. 좌표 범위는 0 이상 1,000 이하이다.

3. x1 < x2, y1 < y2 가 항상 보장된다.

입력

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫째 줄에는 첫 번째 Air View의 x1, y1, x2, y2 값이 주어지며,

두 번째 줄에는 두 번째 Air View의 x1, y1, x2, y2 값이 주어진다.

출력

테스트 케이스 T에 대한 결과는 "#T"를 찍고, 한 칸 띄고, 정답을 출력한다.
(T는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

