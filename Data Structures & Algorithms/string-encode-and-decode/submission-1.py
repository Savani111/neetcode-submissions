class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""

        for word in strs:
            encode += str(len(word)) + "#" + word
        return encode


    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i+= 1

            num = int(length)
            i += 1
            word = s[i : i + num]
            
            decode.append(word)

            i += num
                
        return decode

        
