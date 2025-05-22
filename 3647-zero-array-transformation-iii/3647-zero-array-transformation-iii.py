class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n,q = len(nums), len(queries)
        q_end = [[] for _ in range(n)]

        for query in queries:
            q_end[query[0]].append(query[1])

        pq = []

        cnt_q = [0] * (n+1)
        dec = 0

        for i in range(n):
            dec += cnt_q[i]

            for end in q_end[i]:
                heapq.heappush(pq, -end)
            
            x=nums[i]
            while x > dec and pq and -pq[0] >= i:
                k = -heapq.heappop(pq)
                cnt_q[k+1] -= 1
                dec += 1
            
            if x > dec:
                return -1
        
        return len(pq)