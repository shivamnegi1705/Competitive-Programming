# Question Link:- https://leetcode.com/problems/maximum-number-of-visible-points/

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        # destructuring observer location co-ordinates.
        xc,yc = location
        
        # extra -- to count the points which collide completely with given location
        # These points are always added to the final ans
        extra = 0
        
        # finding all the angles.
        arr = []
        
        for x,y in points:
            #  given point collides with given location
            if x==xc and y==yc:
                extra+=1
                continue
            # theta = tan inverse((y-yc)/(x-xc))
            arr.append(math.atan2(y - yc, x - xc))
            
        # converting angle of view into radians
        angle = math.pi * angle / 180
        
        arr = arr + [x + 2.0 * math.pi for x in arr]
        
        # left pointer
        l = 0
        
        # final ans
        ans = 0
        
        arr.sort()
        
        # applying sliding window to find max size window
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans + extra
