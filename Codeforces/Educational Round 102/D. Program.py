# Question Link:- https://codeforces.com/contest/1473/problem/D

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    s = input()
    query = []
    for i in range(m):
        query.append(list(map(int,input().split())))
    
    pre,suff = [[] for i in range(n)],[[] for i in range(n)]
    values =[]
    cur,mn,mex = 0,0,0
    for i in range(n):
        if s[i]=='+':
            cur+=1
        else:
            cur-=1
        values.append(cur)
        mn,mex = min(mn,cur),max(mex,cur)
        pre[i] = [mn,mex]
    
    cur,mn,mex = 0,0,0
    for i in range(n-1,-1,-1):
        if s[i]=='+':
            mex+=1
            mn+=1
        else:
            mex-=1
            mn-=1
        mn,mex = min(mn,cur),max(mex,cur)
        suff[i] = [mn,mex]
    for i in query:
        l,r = i
        l-=1
        r-=1
        mn1,mex1 = 0,0
        mn2,mex2 = 0,0
        cur = 0
        if l-1>=0:
            mn1 = pre[l-1][0]
            mex1 = pre[l-1][1]
            cur = values[l-1]
        if r+1<n:
            mn2 = cur+suff[r+1][0]
            mex2 = cur+suff[r+1][1]
        mn = min(mn1,mn2)
        mex = max(mex1,mex2)
        print(mex-mn+1)
