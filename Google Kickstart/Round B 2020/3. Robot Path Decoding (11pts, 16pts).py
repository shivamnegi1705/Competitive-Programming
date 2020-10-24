# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d83dc

nums = '23456789'
mod = 10**9
for t in range(int(input())):
    word = input()
    word = '('+word+')'
    stack = []
    ans = ''
    d,r = 0,0
    for i in word:
        if i!=')':
            stack.append(i)
        else:
            temp = ''
            d,r = 0,0
            while True:
                if stack[-1]=='(':
                    stack.pop()
                    break
                else:
                    cur = stack[-1]
                    if type(cur)==list:
                        d,r = d+cur[0],r+cur[1]
                    else:
                        if cur=='N':
                            d-=1
                        elif cur=='S':
                            d+=1
                        elif cur=='E':
                            r+=1
                        else:
                            r-=1
                    stack.pop()
            # stack.append([d,r])
            if stack!=[]:
                # print('last:-',stack[-1])
                if stack[-1] in nums:
                    x = stack[-1]
                    stack.pop()
                    d,r = d*int(x),r*int(x)
                    stack.append([d,r])
            else:
                stack.append([d,r])
        # print(stack)
    # print(cur,stack)
    d,r = 1+d,1+r
    a,b,mod = 0,0,10**9
    if(d<0):
        a=1
    if(r<0):
        b = 1
    r = abs(r)%mod
    d = abs(d)%mod
    if(a==1):
        d = mod-d+1
    else:
        d+=1
    if(b==1):
        r = mod-r+1
    else:
        r+=1
    r-=1
    d-=1
    if(r==0):
        r = mod
    if(d==0):
        d = mod

    
    print("Case #"+str(t+1)+':',r,d)
