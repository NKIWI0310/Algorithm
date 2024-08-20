#n 갯수만큼의 A를 만들려면 어떻게 해야하는가 최적으로 구하기
# 1 의 경우는 0
# 2 의 경우는 2
# 3 의 경우는 3
# 4의 경우는 4
# 5의 경우는 5
#.. 8의 경우는 6
#.. 9의 경우는 6 흠..
#.. 16의 경우는 8이겠지? 


class Solution(object):
    def minSteps(self, n):
        if n == 1:
            return 0
        
        ans = 0
        cur = 2 

        while cur <= n:
            if n % cur == 0:
                ans += cur
                n //= cur
            else:
                cur += 1
                
        return ans
        
        return ans