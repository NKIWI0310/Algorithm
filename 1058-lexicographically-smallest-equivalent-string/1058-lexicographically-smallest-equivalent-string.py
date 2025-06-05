class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = {}

        for c in range(26):
            parent[chr(ord('a')+ c)] = chr(ord('a')+c)
        
        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return
            
            if rootA < rootB:
                parent[rootB] = rootA
            else:
                parent[rootA] = rootB
        
        for a, b in zip(s1,s2):
            union(a,b)
        
        result = []
        for c in baseStr:
            result.append(find(c))
        
        return ''.join(result)