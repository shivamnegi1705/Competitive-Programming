# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

for t in range(int(input())):
    n,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    ans = 0
    for i in arr:
        if c>=i:
            c-=i
            ans+=1
        else:
            break
    print("Case #"+str(t+1)+': '+str(ans))
