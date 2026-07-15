class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            for j, c in enumerate(needle):
                if c != haystack[i + j]:
                    break
                if j == len(needle) - 1 and c == haystack[i + j]:
                    return i
        return -1