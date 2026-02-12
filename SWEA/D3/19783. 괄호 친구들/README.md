19783. - boss 문제 - 괄호 친구들
[링크](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AY18Bjd6DWoDFAWX&solveclubId=AZvefmuKBurHBIN6&problemBoxTitle=String+%28Parsing%29&problemBoxCnt=9&probBoxId=AZwwgEZ67ojHBIPa)
    
문제 내용

시간 : 1개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 1초 / Python의 경우 30초

메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

중괄호 {  } 와 대괄호 [  ]가 섞여있는 문자열이 있습니다.

중괄호와 대괄호 안에는 숫자들이 적혀있습니다.

832be1e43b815e4e96a74aacc81f597b.png

왼쪽부터 오른쪽으로 Parsing을 하며, 중괄호 / 대괄호 안에 있는 숫자들로 연산을 하려고 합니다.

대괄호[ ] 가 나오면 합을 구하면 되고,

중괄호{ } 가 나오면 곱을 구하면 됩니다.

위 예제에서는 [10] {3} [20] [10] {2} 를 구할 수 있으며

1. 0 + [10] = 10

2. 10 x {3} = 30

3. 30 + [20] = 50

4. 50 + [10] = 60

5. 60 x {2} = 120

따라서 정답은 120 입니다.

Parsing 후 연산 결과를 출력 해 주세요.

[세부조건]

1. 연산의 결과에 해당하는 수 n은 1 <= n <= 10,000을 만족합니다.

2. 숫자는 모두 양수로 구성되어 있습니다.

3. 괄호가 부정확한 데이터는 입력되지 않습니다.

4. 괄호 안에는 모두 숫자로 구성되어 있습니다.

입력

첫 번째 줄에 Parsing을 진행할 문자열이 주어집니다.

출력

괄호에 맞게 연산된 결과를 출력합니다.