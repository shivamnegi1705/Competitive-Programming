# Question Link:- https://leetcode.com/problems/video-stitching/
  
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        mn = 0
        mex = 0
        ans = 0
        while mn<T:
            mex = -1
            for i in range(len(clips)):
                if clips[i][0]<=mn and clips[i][1]>mn:
                    mex = max(mex,clips[i][1])
            if mex==-1:
                return -1
            mn = mex
            ans+=1
        return ans
