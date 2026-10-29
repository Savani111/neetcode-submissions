class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for st in strs :
            val = ''.join(sorted(st))
            group[val].append(st)
        
        return list(group.values())
        