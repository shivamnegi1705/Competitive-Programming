# Question Link:- https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003379bb#problem

for test in range(int(input())):
    n,m = list(map(int,input().split()))
    mat = []
    for i in range(n):
        mat.append(list(map(str,input())))

    d = {}
    for i in range(n):
        for j in range(m):
            if mat[i][j] not in d:
                d[ord(mat[i][j])-ord('A')] = 1
    
    graph = [[] for i in range(26)]
    # if a is on top of b then b must be placed before a
    # then b is requirement of a. Then add a-->b
    # if there is a cycle then print -1
    # otherwise find topological sort.
    indeg = [0 for i in range(26)]
    for i in range(n-1):
        for j in range(m):
            x,y = ord(mat[i][j])-ord('A'),ord(mat[i+1][j])-ord('A')
            if x==y:
                continue
            graph[x].append(y)
            indeg[y]+=1
    q = []
    for i in range(26):
        if i not in d:
            continue
        if indeg[i]==0 and d[i]==1:
            q.append(i)
    topsort = []
    cnt = 0
    while q!=[]:
        cur = q[0]
        q.pop(0)
        topsort.append(chr(ord('A')+cur))
        cnt+=1
        for i in graph[cur]:
            indeg[i]-=1
            if indeg[i]==0:
                q.append(i)
    if cnt!=len(d):
        print('Case #'+str(test+1)+':',-1)
    else:
        topsort = topsort[-1::-1]
        ans = ''
        for i in topsort:
            ans+=i
        print('Case #'+str(test+1)+':',ans)
