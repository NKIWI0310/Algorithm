from collections import defaultdict

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        a = Counter(s)
        max_odd = max(n for n in a.values() if n % 2 == 1)
        min_even = min(n for n in a.values() if n % 2 == 0)
        return max_odd - min_even
        
        
