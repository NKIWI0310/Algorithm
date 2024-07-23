class Solution(object):
    def frequencySort(self, nums):
        dic = defaultdict(int)

        for i in nums:
            dic[i] += 1
        
        sDic = sorted(dic.items(), key = lambda item : (item[1], -item[0]))
        
        ans = []

        for k,v in sDic:
            for _ in range(0,v):
                ans.append(k)
                
        return ans
        
        
