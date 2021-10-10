for _ in range(int(input())):
    s = input().split()
    firstBalloon = int(s[0])
    secondBalloon = int(s[1])
    n = int(input())
    firstQuestion = 0
    secondQuestion = 0
    for i in range(n):
        s2 = input().split()
        firstQuestion = firstQuestion+int(s2[0])
        secondQuestion = secondQuestion+int(s2[1])
    print(min((firstQuestion*firstBalloon+secondQuestion*secondBalloon),
              (firstQuestion*secondBalloon+secondQuestion*firstBalloon)))
