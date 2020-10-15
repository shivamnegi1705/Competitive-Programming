# Question Link:- https://codeforces.com/contest/1430/problem/D
import heapq
for _ in range(int(input())):
    n = int(input())
    s = input()
    st = []
    arr = []
    l,r = 0,0
    while l<n:
        r = l
        while r+1<n and s[r+1]==s[l]:
            r+=1
        st.append(l)
        if r-l+1>1:
            arr.append([l,r-l+1])
        l = r+1
    st = st[-1::-1]
    ans = 0
    heapq.heapify(arr)
    while st!=[]:
        x = st.pop()
        if len(arr)==0:
            ans+=1
            if st!=[]:
                st.pop()
        else:
            cur = heapq.heappop(arr)
            if cur[0]==x:
                ans+=1
            else:
                ans+=1
                cur[1]-=1
                if cur[1]>1:
                    heapq.heappush(arr,cur)
    print(ans)
