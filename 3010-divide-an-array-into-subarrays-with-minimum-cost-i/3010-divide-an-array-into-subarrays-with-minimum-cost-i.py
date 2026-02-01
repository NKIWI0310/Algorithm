"""
배열을 받으면 3등분한 후 앞의 값을 더했을 때
가장 작은 값이 나오게 만들면 됨


그런데 가장 앞의 값은 무조건 포함됨
그 이후 가장 작은값 2개를 선택하면 끝 아닌가?
"""

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = 0

        ans += nums[0]
        temp = sorted(nums[1:])
        ans += temp[0] + temp[1]

        return ans

        