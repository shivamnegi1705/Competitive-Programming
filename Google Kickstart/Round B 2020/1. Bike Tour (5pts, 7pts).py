# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            ans+=1
    print("Case #"+str(t+1)+': ',ans)
