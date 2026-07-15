class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        head1 = 0
        head2 = 0

        while(head1 < m + head2 and head2 < n):
            if (nums1[head1] <= nums2[head2]):
                head1 += 1
            else:
                for i in range(m - head1 + head2):
                    nums1[head2 + m - i] = nums1[head2 + m - i - 1]
                nums1[head1] = nums2[head2]
                head1 += 1
                head2 += 1
                
        if head2 <= n - 1:
            for j in range (n - head2):
                nums1[m + head2 + j] = nums2[head2 + j]
                
        print(nums1)        