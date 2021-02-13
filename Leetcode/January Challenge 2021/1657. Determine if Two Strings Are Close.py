# Question Link:- https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, w1, w2):
        return set(w1) == set(w2) and Counter(Counter(w1).values()) == Counter(Counter(w2).values())
