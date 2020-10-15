# Question Link:- 
mex = 1005
save = [[] for i in range(mex)]
can = [False for i in range(mex)]
 
def init():
    for i in range(mex//3+2):
        for j in range(mex//5+2):
            for k in range(mex//7+2):
                val = i*3 + j*5+k*7
                if val<=1000:
                    can[val] = True
                    save[val] = [i,j,k]
init()
for _ in range(int(input())):
    n = int(input())
    if can[n]:
        print(*save[n])
    else:
        print(-1)
