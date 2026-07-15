class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0                  # 先頭から走査するポインタ
        p2 = len(nums) - 1      # 末尾から走査するポインタ
        
        while(p1 <= p2):
            if nums[p1] == val:
                nums[p1] = nums[p2]
                p2 -= 1
            else:
                p1 += 1
                
        return p1 - 1