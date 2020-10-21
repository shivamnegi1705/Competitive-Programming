# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387174

for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    inc, dec = 0, 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc += 1
            dec = 0
        if arr[i] < arr[i - 1]:
            dec += 1
            inc = 0
        if inc >= 4:
            ans += 1
            inc = 0
        if dec >= 4:
            ans += 1
            dec = 0
    print('Case #' + str(t + 1) + ':', ans)
