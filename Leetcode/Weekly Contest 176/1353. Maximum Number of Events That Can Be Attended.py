# Question Link:- https://leetcode.com/contest/weekly-contest-176/problems/maximum-number-of-events-that-can-be-attended/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        # sort events by their end time.
        arr = []
        for i in events:
            arr.append([i[1],i[0]])
        arr.sort()
        for i in range(len(events)):
            arr[i] = [arr[i][1],arr[i][0]]
        
        # pick nearest day available which is greater than equal to start day
        ans = 0
        uni = []
        for i in range(1,100001):
            uni.append(i)
        
        # function which will find the nearest available day greater than equal to start time given
        def binarysearch(st,array):
            lo = 0
            hi = len(array)-1
            while lo<hi:
                mid = (lo+hi)//2
                if array[mid]<st:
                    lo = mid
                else:
                    hi = mid
                if hi-lo==1:
                    break
            if array[lo]>=st:
                return lo
            elif array[hi]>=st:
                return hi
            return -1
            
        
        for i in arr:
            # start time and end time
            st,en = i
            # if no day is available
            if len(uni)==0:
                continue
            # find index for the next available day.
            it = binarysearch(st,uni)
            # if it==-1 means no day is available
            # uni[it]>en means nearest day available is greater than end time so we can not choose this task.
            if it==-1 or uni[it]>en:
                continue
            # we can do current task on uni[it] day so pop this day.
            else:
                uni.pop(it)
                ans+=1
        
        return ans
