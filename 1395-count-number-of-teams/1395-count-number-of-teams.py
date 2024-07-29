#문제는 문자열이 주어지면, 3명의 병사가 내림차순 혹은 오름차순으로 배열 될 수 있는 가짓수를 구하는 것
#


class Solution(object):
    def numTeams(self, rating):
        n = len(rating)
        
        lessBefore = [0] * n
        greaterBefore = [0] * n
        lessAfter = [0] * n
        greaterAfter = [0] * n

        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    lessBefore[i] +=1
                elif rating[j] > rating[i]:
                    greaterBefore[i] +=1
        
        for i in range(n):
            for j in range(i+1, n):
                if rating[j] < rating[i]:
                    lessAfter[i] +=1
                elif rating[j] > rating[i]:
                    greaterAfter[i] +=1
        
        cnt = 0

        for i in range(n):
            cnt += lessBefore[i] * greaterAfter[i]
            cnt += greaterBefore[i] * lessAfter[i]
        
        return cnt

                