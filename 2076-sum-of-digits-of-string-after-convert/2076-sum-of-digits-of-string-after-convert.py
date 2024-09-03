'''
string s 는 소문자로 이루어져있다. 
s를 숫자로 대응할 생각이다 
a - > 1 b - > 2 이런식이다 
97이 소문자 a임

변환 후에는 각 숫자를 1자리로 더할 생각이다.
이는 k번 진행 할 것이다.
'''

class Solution(object):
    def getLucky(self, s, k):
        
        nS = ""

        for i in range(len(s)):
            nS += str(ord(s[i]) - 96)
        
        for _ in range(k):
            temp = 0
            for i in range(len(nS)):
                temp += int(nS[i])
            nS = str(temp)

        return int(nS)
        