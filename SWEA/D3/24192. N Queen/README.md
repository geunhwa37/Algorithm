24192. N Queen
[링크](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZvefmuKBurHBIN6&contestProbId=AZWmjHXaTmLHBIPl&probBoxId=AZzff0HahavHBIRj&type=USER&problemBoxTitle=%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9&problemBoxCnt=2)
       
문제 내용

시간 : 1개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 1초 / Python의 경우 3초

메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

체스에서 Queen은 다음 이미지와 같이 가로, 세로, 대각선 방향으로 자유롭게 이동할 수 있습니다.

 

chess1.png
 

 

N x N 크기의 체스판에서, N개의 Queen을 배치하고자 합니다.

N개의 Queen은 서로 공격할 수 없는 곳에 배치해야 합니다.

만약 Queen이 이동할 수 있는 곳에 다른 Queen이 있다면, 이는 공격 가능한 것으로 간주합니다.

 

아래 이미지는 N = 8 인 경우, 가능한 배치입니다.

아래 배치 뿐만 아니라, 다양한 경우가 있을 수 있습니다.

chess2.pngchess3.png
 

 

N 이 주어졌을 때, 서로 공격이 불가능하도록 배치할 수 있는 경우의 수를 출력해 주세요.


[입력]

N을 입력 받습니다. (1 <= N <= 13)

[출력]

서로 공격할 수 없도록

배치할 수 있는 경우의 수를 출력하세요.