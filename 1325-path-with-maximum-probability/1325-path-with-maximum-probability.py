#무방향 그래프가 주어짐
#edge와 그에 맞는 가중치(가능성)들이 주어짐
#start와 end가 주어지며 
#start와 end로 갈 때 가장 높은 방향을 고름

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        dist = [0] * n
        dist[start_node] = 1

        for _ in range(n):    
            stop = False

            for i, (u,v) in enumerate(edges):
                if dist[v] < dist[u] * succProb[i]:
                    dist[v] = dist[u] * succProb[i]
                    stop = True

                if dist[u] < dist[v] * succProb[i]:
                    dist[u] = dist[v] * succProb[i]
                    stop = True

            if stop == False:
                break

        return dist[end_node]


