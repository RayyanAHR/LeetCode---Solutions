class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new_nums1 = set(nums1)
        common = set()

        for x in nums2:
            if x in new_nums1:
                common.add(x)
        return list(common)


