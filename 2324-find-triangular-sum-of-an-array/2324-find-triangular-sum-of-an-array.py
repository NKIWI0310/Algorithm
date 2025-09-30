"""
계속 2개 자리 숫자를 더하면서 가장 마지막으로 남는 1의 자리 숫자를 반환하는 함수를 짜란 소리

"""


class Solution(object):
    def triangularSum(self, nums):
        def binomial_coefficient(n, k):
            res = 1
            for i in range(1, k + 1):
                res = res * (n - i + 1) // i
            return res

        n = len(nums)
        result = 0
        for i in range(n):
            coeff = binomial_coefficient(n - 1, i)
            result += coeff * nums[i]
        return result % 10
