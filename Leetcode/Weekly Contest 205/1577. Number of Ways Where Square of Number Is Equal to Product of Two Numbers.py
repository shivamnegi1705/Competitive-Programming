# Question link:- https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # maps to store square of elements of nums1 and nums2.
        mapper1 = {}
        mapper2 = {}
        
        # Traversing nums1 and mapping squares into map
        for i in nums1:
            x = i**2
            if x in mapper1:
                mapper1[x]+= 1
            else:
                mapper1[x] = 1

        # Traversing nums1 and mapping squares into map
        for i in nums2:
            x = i**2
            if x in mapper2:
                mapper2[x]+=1
            else:
                mapper2[x] = 1
        
        # ans--> to count number of valid triplets
        ans = 0
        
        # Finding val = nums2[i]*nums2[j], if it is present in mapper1 then increase count by frequency of val.
        for i in range(len(nums2)):
            for j in range(len(nums2)):
                if i<j:
                    x = nums2[i]*nums2[j]
                    if x in mapper1:
                        ans+=mapper1[x]
        
        # Finding val = nums2[i]*nums2[j], if it is present in mapper1 then increase count by frequency of val.
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if i<j:
                    x = nums1[i]*nums1[j]
                    if x in mapper2:
                        ans+=mapper2[x]
        return ans
        
        
