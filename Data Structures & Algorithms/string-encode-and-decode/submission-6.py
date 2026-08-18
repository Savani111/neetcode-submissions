class Solution:

    def encode(self, strs: List[str]) -> str:
            st = ""

            for word in strs:
                num = len(word)
                st += str(num) + "%" + word
            return st

    def decode(self, s: str) -> List[str]:
        strs = [] 
        i = 0
        while i < len(s):
            j = i
            while s[j] != "%":
                j += 1

            num = int(s[i:j])
            word = ""
            for val in range(j+1, j + num + 1):
                word += s[val]
            strs.append(word)
            i = num + j + 1
            
        return strs



