class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        
        #firstable, remove the space
        for i in range(l):
            if s[(l - 1) - i] != ' ':
                break
        
        #Secondary, count the length of the word
        for j in range(l):
            if s[(l - 1) - i - j] == ' ':
                break
            if (l - 1) - i - j == 0:
                j += 1
                break

        return j