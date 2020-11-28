# Question Link:- https://leetcode.com/problems/design-front-middle-back-queue/

from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.st1 = deque([])
        self.st2 = deque([])

    def pushFront(self, val: int) -> None:
        if len(self.st1)==len(self.st2):
            self.st1.appendleft(val)
            x = self.st1.pop()
            self.st2.appendleft(x)
            
        else:
            self.st1.appendleft(val)
        
    def pushMiddle(self, val: int) -> None:
        if len(self.st1)==len(self.st2):
            self.st2.appendleft(val)
        else:
            self.st1.append(val)
        
    def pushBack(self, val: int) -> None:
        if len(self.st1)==len(self.st2):
            self.st2.append(val)
        else:
            x = self.st2.popleft()
            self.st1.append(x)
            self.st2.append(val)
        
    def popFront(self) -> int:
        if len(self.st1)==0 and len(self.st2)==0:
            return -1
        if len(self.st1)==len(self.st2):
            x = self.st1.popleft()
            return x
        else:
            if len(self.st1)==0:
                x = self.st2.pop()
                return x
            else:
                x = self.st1.popleft()
                y = self.st2.popleft()
                self.st1.append(y)
                return x
        
    def popMiddle(self) -> int:
        if len(self.st1)==0 and len(self.st2)==0:
            return -1
        if len(self.st1)==len(self.st2):
            x = self.st1.pop()
            return x
        else:
            x = self.st2.popleft()
            return x
        
    def popBack(self) -> int:
        if len(self.st1)==0 and len(self.st2)==0:
            return -1
        if len(self.st1)==len(self.st2):
            x = self.st2.pop()
            y = self.st1.pop()
            self.st2.appendleft(y)
            return x
        else:
            x = self.st2.pop()
            return x
