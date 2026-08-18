class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}

        for char in s:
            mp[char] = mp.get(char, 0) + 1

        for char in t:
            if mp.get(char, 0) <= 0:
                return False
            mp[char] -= 1
        return True