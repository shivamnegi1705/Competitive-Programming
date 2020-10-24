# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83bf

for t in range(int(input())):
    n,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    for i in range(n-1,-1,-1):
        d = d-(d%arr[i])
    ans = d
    print("Case #"+str(t+1)+': ',ans)
