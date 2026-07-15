class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        prefix = ""
        
        for i, c in enumerate(strs[0]):
            for j in range(1, n):
                if len(strs[j]) <= i:
                    return prefix
                if strs[j][i] != c:
                    return prefix
            prefix += c
            
        return prefix