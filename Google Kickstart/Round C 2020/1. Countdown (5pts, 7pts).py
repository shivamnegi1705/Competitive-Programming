# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2

maxn = 200005
for p in range(int(input())):
    n,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    f = 0
    cnt = 0
    ans = 0
    prev = -1
    for i in arr:
        if i==k:
            cnt = 1
            prev = k-1
            f = 1
        else:
            if f==1:
                if prev==i:
                    cnt+=1
                    prev-=1
                else:
                    f = 0
                    cnt = 0 
                if cnt==k:
                    f = 0
                    cnt = 0
                    ans+=1
                
    print('Case #'+str(p+1)+':',ans)
