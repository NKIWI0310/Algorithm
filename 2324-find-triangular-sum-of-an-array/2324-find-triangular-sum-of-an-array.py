class Solution(object):
    def triangularSum(self, nums):
        def bionomial_coefficient(n,k):
            res = 1
            for i in range(1,k+1):
                res = res * (n-i+1) // i
            return res

        n = len(nums)
        result = 0

        for i in range(n):
            coeff = bionomial_coefficient(n-1,i)
            result += (coeff * nums[i])
            result = result % 10

        return result
