'''
가장 간단한 느낌
일단 작은 순서대로 배열을 정렬하고 
더하면서 못하는 시점에 false
'''

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        tmp = mass

        asteroids.sort()

        for i in range(len(asteroids)):
            if tmp >= asteroids[i]:
                tmp += asteroids[i]
            else:
                return False
        
        return True 

            

         