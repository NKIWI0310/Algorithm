'''
문제: 일부 문자를 삭제해서 가장 긴 k보다 작은 2진수 구하기


'''

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        n = len(s)
        zeros = s.count('0')
        ones = 0
        value = 0
        power = 1

        for i in range(n -1, -1, -1):
            if s[i] == '1':
                if value + power > k:
                    continue
                value += power
                ones += 1
            power <<= 1 #제곱 연산
            if power > k:
                break
        
        return zeros + ones
