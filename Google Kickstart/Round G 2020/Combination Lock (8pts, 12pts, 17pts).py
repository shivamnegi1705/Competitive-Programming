# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414a24

# Solution for 8pts and 12pts.

for t in range(int(input())):
    w, n = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = -1
    for i in arr:
        cur = 0
        for j in arr:
            l = abs(i-j)
            r = n-l
            cur += min(l, r)
        if ans==-1 or cur<ans:
            ans = cur
    print("Case #" + str(t + 1) + ":", ans)
