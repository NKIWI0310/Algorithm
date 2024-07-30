class Solution(object):
    def minimumDeletions(self, s):
        n = len(s)
        bCount = [0] * (n + 1)
        aCount = [0] * (n + 1)
        
        # b누적
        for i in range(n):
            bCount[i + 1] = bCount[i] + (1 if s[i] == 'b' else 0)

        # a누적 
        for i in range(n - 1, -1, -1):
            aCount[i] = aCount[i + 1] + (1 if s[i] == 'a' else 0)

        # 최소 삭제 횟수 계산
        minDeletions = float('inf')
        for i in range(n + 1):
            minDeletions = min(minDeletions, bCount[i] + aCount[i])

        return minDeletions
