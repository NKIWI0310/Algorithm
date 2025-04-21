"""

upper - lower 은 가장 큰 값
maxNum - minNum 은 누적 큰 값 작은 값의 최대

"""

class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        """
        :type differences: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        a = maxNum = minNum = 0

        for diff in differences:
            a += diff
            maxNum = max(maxNum, a)
            minNum = min(minNum, a)
        
        return max(0, (upper - lower) - (maxNum - minNum) + 1)
            
        