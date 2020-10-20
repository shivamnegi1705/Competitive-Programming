# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb

for t in range(int(input())):
    s = input()
    n = len(s)
    cnt = [0 for i in range(n)]
    for i in range(n):
        if s[i:i+5]=='START':
            cnt[i]+=1
    for i in range(n-2,-1,-1):
        cnt[i] = cnt[i]+cnt[i+1]
    ans = 0
    for i in range(n):
        if s[i:i+4]=="KICK":
            ans+=cnt[i]
    print('Case '+"#"+str(t+1)+":",ans)
