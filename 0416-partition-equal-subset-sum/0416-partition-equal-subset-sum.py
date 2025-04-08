class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        2개의 배열로 나누었을 때 각 배열의 합이 같은지 판단
        1. 우선 합이 짝수여야 함
        2. DP로 접근 target만 만족하면 되기에 한쪽만 target에 도달해도 반으로 쪼개질 수 있기에 무조건 도달하는지 여부만 파악
        """

        total = sum(nums)

        if total % 2 == 1: 
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target]



        
