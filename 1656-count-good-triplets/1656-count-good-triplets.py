class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0

        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if abs(arr[i] - arr[j]) <= a:
                        if abs(arr[j]-arr[k]) <= b:
                            if abs(arr[k]- arr[i]) <= c:
                                ans += 1

        return ans