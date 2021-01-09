# Question Link:- https://leetcode.com/problems/maximum-score-from-removing-substrings/

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st = []
        ans = 0
        
        cur = 'ab'
        val = x
        if y>val:
            val = y
            cur = 'ba'
        
        f = 0
        
        while True:
            for i in s:
                if st==[]:
                    st.append(i)
                else:
                    if st[-1]+i==cur:
                        st.pop()
                        ans+=val
                        f = 1
                    else:
                        st.append(i)
            if f==0:
                break
            s = ''
            for i in st:
                s+=i
            st = []
            f = 0

        st = []
        f = 0
        while True:
            for i in s:
                if st==[]:
                    st.append(i)
                elif cur=='ba':
                    if st[-1]+i=='ab':
                        st.pop()
                        ans+=x
                        f = 1
                    else:
                        st.append(i)
                elif cur=='ab':
                    if st[-1]+i=='ba':
                        st.pop()
                        ans+=y
                        f = 1
                    else:
                        st.append(i)
                else:
                    st.append(i)
            if f==0:
                break
            s = ''
            for i in st:
                s+=i
            st = []
            f = 0
        return ans
