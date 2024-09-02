'''
문제를 정리하자면 

학생들 마다 chalk의 분필을 사용하여 문제를 푼다
총 k개의 분필이 존재하고, 분필의 갯수가 음수가 되는 사람이 있다면
그 사람이 분필을 교체해야하는 사람이다.

분필을 교체하는 사람을 반환해라
'''

class Solution(object):
    def chalkReplacer(self, chalk, k):
        
        cnt = len(chalk)
        total = 0

        for j in range(cnt):
            total += chalk[j]
        
        if k > total:
            k = k % total

        for j in range(cnt):
            k -= chalk[j]

            if k < 0:
                return j
        
        return 0
        
            

        
        