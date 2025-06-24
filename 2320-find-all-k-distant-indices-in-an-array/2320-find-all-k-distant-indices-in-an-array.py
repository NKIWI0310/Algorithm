'''
생각핸 해결 방법
1. key를 간격으로 k만큼 true로 만들어주고, true의 길이를 반환하면 일단 될 문제긴함
하지만 1번은 중복되는 것에 대한 불필요한 연산이 있을 수동

'''
class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        result = []
        n = len(nums)
        
        mark = [False] * n        
        for i in range(n):
            if nums[i] == key:
                start = max(0, i - k)
                end = min(n - 1, i + k)
                for j in range(start, end + 1):
                    mark[j] = True
        
        for i in range(n):
            if mark[i]:
                result.append(i)
        
        return result
