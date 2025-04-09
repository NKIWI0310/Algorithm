class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        newN = sorted(set(nums))
        result = 0

        if k > min(newN):
            return -1

        for i in range(len(newN)):
            if newN[i] > k:
                result += 1

        if result == 0 and len(newN) != 1:
            result = -1

        return result
        
        