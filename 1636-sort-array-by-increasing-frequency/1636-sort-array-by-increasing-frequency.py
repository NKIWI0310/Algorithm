class Solution(object):
    def frequencySort(self, nums):
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        
        sDic = sorted(nums, key=lambda x: (dic[x], -x))
        
        return sDic
        
