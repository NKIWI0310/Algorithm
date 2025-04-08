class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        visited = [False] * 101

        for i in range(len(nums)-1, -1, -1):
            if visited[nums[i]]:
                return i // 3 + 1
            visited[nums[i]] = True
        
        return 0
        

        
            