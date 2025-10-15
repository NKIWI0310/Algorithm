class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums) #개수만 큼
        
        cnt = 1
        tempCnt = 0
        ans = 0

        for i in range(1,n):
            if nums[i] > nums[i-1]: #만약 값이 크다면 계속 증가한다는 의미
                cnt += 1
            else:
                tempCnt, cnt = cnt, 1
            ans = max(ans, cnt // 2)
            ans = max(ans, min(cnt, tempCnt)) 

        return ans