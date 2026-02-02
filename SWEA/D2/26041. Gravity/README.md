[문제 링크](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZvefmuKBurHBIN6&contestProbId=AZwcC1C6b6_HBIT3&probBoxId=AZwcBnDqb1HHBIT3&type=USER&problemBoxTitle=2%EC%9B%94+2%EC%9D%BC+%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C&problemBoxCnt=2)

시간 : 3개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 1초 / Python의 경우 3초

메모리 : 힙, 정적 메모리 합쳐서 262144 kbytes 이내, 스택 메모리 1024 kbytes 이내

가로 N 세로 100 크기의 방에 상자들이 쌓여있다. 
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 가장 큰 낙차를 구하여라

[제약 사항]

중력은 회전이 완료된 후 적용된다.
상자들은 모두 한쪽 벽면에 붙여진 상태로 쌓여 2차원의 형태를 이루며 벽에서 떨어져서 쌓인 상자는 없다.
방의 세로 길이는 항상 100이다. 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 줄에는 방의 가로길이가 주어지고 그 다음 줄부터는 쌓여있는 상자의 수가 주어진다.


[출력]

부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.


[그림 설명]

총 26개의 상자가 회전 후, 오른쪽 방 그림의 상태가 된다. A 상자의 낙차가 7로 가장크므로 7을리턴하면 된다.
회전 결과, B상자의 낙차는6, C상자의 낙차는 1이다.

