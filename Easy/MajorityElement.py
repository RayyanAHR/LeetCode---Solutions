class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1
        
            if count[x] > len(nums) // 2:
                return x
