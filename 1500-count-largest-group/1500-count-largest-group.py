from collections import defaultdict

class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_map = defaultdict(int)

        for i in range(1, n + 1):
            key = sum(int(x) for x in str(i))
            count_map[key] += 1

        max_value = max(count_map.values())
        count = sum(1 for v in count_map.values() if v == max_value)

        return count
