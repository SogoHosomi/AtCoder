class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0
        candidate = 0
        
        for num in nums:
            if counter == 0:
                candidate = num
                
            if candidate == num:
                counter += 1
            else:
                counter -= 1
                
        return candidate
            
        
        