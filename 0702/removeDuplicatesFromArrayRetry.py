class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        l = len(nums)
        head = 0

        for tail in range(1, l):
            if nums[head] != nums[tail]:
                nums[head + 1] = nums[tail]
                head += 1
    
        return head + 1