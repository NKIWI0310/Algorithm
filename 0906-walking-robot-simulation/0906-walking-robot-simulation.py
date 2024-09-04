class Solution(object):
    def robotSim(self, commands, obstacles):
        obstacles = set(map(tuple, obstacles))  # Set으로 변환하여 검색 속도 최적화
        answer = 0
        x, y = 0, 0
        cDir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cIdx = 0

        for command in commands:
            if command > 0:  # 이동 처리
                for _ in range(command):
                    nX = x + cDir[cIdx][0]
                    nY = y + cDir[cIdx][1]
                    if (nX, nY) not in obstacles:
                        x, y = nX, nY
                        answer = max(answer, x**2 + y**2)
                    else:
                        break
            else:  # 방향 처리
                if command == -1:  # 오른쪽 90도 회전
                    cIdx = (cIdx + 1) % 4
                else:  # 왼쪽 90도 회전
                    cIdx = (cIdx - 1) % 4

        return answer
