class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        start_idx = 0
        result, current_sum = 0,0

        for end_idx in range(n):
            current_sum += nums[end_idx]

            while start_idx <= end_idx and current_sum * (end_idx-start_idx+1) >=k:
                current_sum -= nums[start_idx]
                start_idx +=1
            
            result += end_idx - start_idx + 1
        
        return result
        