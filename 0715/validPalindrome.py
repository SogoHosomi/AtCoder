class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re        
        final_s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        if final_s == '':
            return True

        for i, c in enumerate(final_s):
            if c != final_s[-(i + 1)]:
                return False
            if i >= -(-len(final_s) // 2) - 1:
                return True