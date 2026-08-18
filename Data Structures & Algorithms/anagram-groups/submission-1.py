class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            mp = {}
            for char in word:
                mp[char] = mp.get(char, 0) + 1
            key = tuple(sorted(mp.items()))
        
            if key not in group:
                group[key] = []
            group[key].append(word)
        return list(group.values())
            