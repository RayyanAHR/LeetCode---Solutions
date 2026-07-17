class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1

        for j in t:
            count[j] = count.get(j, 0) - 1

        for x in count.values():
            if x != 0:
                return False
        
        return True
