class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        m = defaultdict(int)
        
        for num in nums:
            m[num] += 1
            
        for key, value in m.items():
            if value > n/2:
                return key
            