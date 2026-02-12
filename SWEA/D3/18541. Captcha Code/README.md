18541. Captcha Code
[링크](https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AZvefmuKBurHBIN6&contestProbId=AYoUx5EaMDEDFAU6&probBoxId=AZwb8CG6bUnHBIT3&type=USER&problemBoxTitle=im+%EA%B8%B0%EC%B6%9C+%EB%AC%B8%EC%A0%9C&problemBoxCnt=5)

문제 내용

시간 : 10개 테스트케이스를 합쳐서 C의 경우 1초 / C++의 경우 1초 / Java의 경우 1초 / Python의 경우 3초

메모리 : 힙, 정적 메모리 합쳐서 256MB 이내, 스택 메모리 1MB 이내

AI의 발전으로 인해 세상의 많은 것이 편해졌다.

하지만 이로 인해 많은 것이 불편해진 것도 있다.

그중 하나가 바로 사이버 범죄가 너무 많이 일어난다는 것이다. 

 

사람들은 AI를 활용해 인터넷상에서 개인정보 해킹 등 여러 방면에서 문제를 일으키고 있다.

그렇기 때문에 많은 웹사이트나 앱 등에서 "사람인가?" 를 인증하기 위한 Captcha Code를 AI가 뚫을 수 없도록 발전시키고 있다. 

 

코코가 개발한 새로운 Captcha Code 생성기는 아래와 같다.

[1] 랜덤으로 N개 길이의 Sample이 주어진다.

[2] 그리고 K개 길이의 PassCode가 주어진다.

[3] 사용자는 Sample에서 PassCode를 "순차적으로" 만들 수 있는지를 검증해야 한다. 

 

코코는 자신이 만든 생성기에 문제가 있는지 없는지 직접 QA 과정을 거치려고 한다.

Sample과 PassCode가 주어졌을때, Sample에서 PassCode를 만들 수 있는지 없는지를 판단하는 프로그램을 작성하라.

 

[예시]

 

Captcha Code 생성기는 아래와 같이 Sample과 PassCode를 생성한다.

아래는 N = 10, K = 4의 Sample과 PassCode의 예시이다.



 

 

사용자는 해당 Sample에서 "순서차적으로' PassCode를 만들 수 있는지를 검증해야 한다. 

위의 예시의 Sample에서는 PassCode를 순서대로 생성할 수 있다.

아래의 이미지의 색을 따라가면, PassCode의 순서대로 Sample에 순차적으로 숨겨저 있는 것을 알 수 있다. 



 

아래는 Sample에서 PassCode를 생성하는 또 다른 예시이다. 

위 또는 아래 예시 모두 순차적으로 Sample에서 PassCode를 생성할 수 있으므로, 1을 출력한다. 



 

 

아래와 같이 다른 Sample과 PassCode가 주어진다고 가정하자. (N = 7, K = 3)



 

위의 경우에는 순차적으로 Sample에서 PassCode를 생성하는 것이 불가능하다. 

그렇기에 0을 출력한다.



 

 

[제약사항] 

5 <= N <= 300,000

3 <= K < N

입력

첫번째 줄에는 테스트 케이스의 개수 T가 주어진다. 

두번째 줄부터 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫번째 줄에는 Sample의 길이 N, PassCode의 길이 K가 주어진다.

각 테스트 케이스의 두번째 줄에는 N개 길이의 Sample이 공백으로 구분되어 주어진다.

각 테스트 케이스의 세번째 줄에는 K개 길이의 PassCode가 공백으로 구분되어 주어진다. 

공백으로 주어지는 값은 0과 9사이의 정수이다.

 

출력

각 테스트 케이 t에 대한 결과를 각 줄에 "#t" (테스트 케이스는 1번부터 시작)을 출력하고, 한 칸을 띄운 다음 정답을 출력한다. 

정답은 만약 Sample에서 PassCode를 생성할 수 있다면 1, 아니면 0을 출력한다. 