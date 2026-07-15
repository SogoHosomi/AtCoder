class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        l = len(nums)
        insertPoint = 0
        head = 0
        tail = 1
        
        while tail < l:
            if nums[head] == nums[tail]:
                tail += 1
            else:
                nums[insertPoint] = nums[head]
                nums[insertPoint + 1] = nums[tail]
                insertPoint += 1
                head = tail
                tail += 1
    
        return insertPoint + 1