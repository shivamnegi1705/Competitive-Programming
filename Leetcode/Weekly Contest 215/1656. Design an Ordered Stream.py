# Question Link:- https://leetcode.com/problems/design-an-ordered-stream/

class OrderedStream:

    def __init__(self, n: int):
        self.arr = ['' for i in range(n)]
        self.ptr = 0
        self.m = n
    def insert(self, idi: int, value: str) -> List[str]:
        self.arr[idi-1] = value
        ans = []
        while self.ptr<self.m:
            if self.arr[self.ptr]!='':
                ans.append(self.arr[self.ptr])
            else:
                return ans
            self.ptr+=1
        return ans
