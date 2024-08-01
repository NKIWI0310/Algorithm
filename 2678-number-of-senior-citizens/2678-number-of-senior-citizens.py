#첫 10자리는 승객의 전번
#두번째는 성 F or M
# 그이후 2개는 나이
# 마지막 2개는 좌석

class Solution(object):
    def countSeniors(self, details):
        ans = 0
        for i in details:
            if int(i[11:13]) > 60:
                ans +=1

        return ans 