# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386d5c
# Solution for 12pts.

for t in range(int(input())):
    n, q = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = []
    for i in range(q):
        start, k = list(map(int, input().split()))
        if start == n:
            ans.append(start - k + 1)
        elif start == 1:
            ans.append(start+k-1)
        else:
            lr = start - 1
            rr = start + 1
            l, r = start - 2, start - 1
            cur = start
            while k > 1:
                if l >= 0 and r < n - 1:
                    if arr[l] < arr[r]:
                        cur = lr
                        lr -= 1
                        l-=1
                    else:
                        cur = rr
                        rr += 1
                        r+=1
                elif l < 0 and r < n - 1:
                    cur = rr
                    rr += 1
                    r+=1
                elif l >= 0 and r == n - 1:
                    cur = lr
                    lr -= 1
                    l-=1
                k -= 1
            ans.append(cur)
    print('Case #' + str(t + 1) + ':',*ans)
