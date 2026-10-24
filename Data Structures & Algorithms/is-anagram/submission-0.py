class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_=list(s)
        t_=list(t)
        return sorted(s_)==sorted(t_)