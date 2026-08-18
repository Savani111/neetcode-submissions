class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for char in s:
            if char.isalnum() :
                word+= char
        word = word.lower()
        half = len(word) // 2

        for i in range(half):
            if (word[i] != word[(len(word) - 1) - i]):
                return False

        return True
