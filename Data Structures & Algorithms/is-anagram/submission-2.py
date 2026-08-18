class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        used = {}

        for c in s:
            used[c] = used.get(c, 0) + 1
        
        for c in t:
            if c not in used:
                return False;

            used[c] -= 1

            if used[c] < 0:
                return False;
        return True;