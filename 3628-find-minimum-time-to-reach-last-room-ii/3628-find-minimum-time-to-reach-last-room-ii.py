class Solution(object):
    def minTimeToReach(self, moveTime):
        row, col = len(moveTime), len(moveTime[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        end = (row - 1, col - 1)

        dist = {}  # (i, j, s) -> 최소 시간
        q = [(0, 0, 0, 1)]  # (시간, 행, 열, 상태)
        heapq.heapify(q)

        while q:
            t, i, j, s = heapq.heappop(q)
            key = (i, j, s)

            if key in dist and dist[key] <= t:
                continue
            dist[key] = t

            if (i, j) == end:
                return t

            ns = s ^ 1  # 상태 전환

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < row and 0 <= nj < col:
                    nt = max(t, moveTime[ni][nj]) + ns + 1
                    heapq.heappush(q, (nt, ni, nj, ns))

        return -1
