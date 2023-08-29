class Solution {
    public int bestClosingTime(String customers) {
        int n = customers.length();

        int[] prefix = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + (customers.charAt(i - 1) == 'N' ? 0 : 1);
        }

        int minDiff = prefix[n]; // 첫 번째 차이는 모두 'N'일 때의 차이
        int bestClosingTime = 0;

        for (int i = 1; i <= n; i++) {
            // 'Y'로 시작하는 문자열의 경우 'Y'의 갯수에 대한 차이와 'N'의 갯수에 대한 차이를 계산
            int diff = i - 2 * prefix[i] + prefix[n];

            if (diff < minDiff) {
                minDiff = diff;
                bestClosingTime = i;
            }
        }
        return bestClosingTime;
    }
}

/*
prefix 는 이전의 값과 모두 N일경우의 차이이다 

YYNY 
NNNN

고로 

prefix[0] 의 경우 0
prefix[1] 의 경우 1
prefix[2] 의 경우 2
prefix[3] 의 경우 2
prefix[4] 의 경우 1
 
i시간 전에 도착한 고객 수는 prefix[i]입니다
i 시간 이후에 도착한 고객 수는 prefix[n] - prefix[i]
페널티는 i 시간 전에 도착하지 않은 고객의 수와 i 시간 후에 도착한 고객의 수의 합
따라서 페널티는 (i - prefix[i]) + (prefix[n] - prefix[i]) = i - 2 * prefix[i] + prefix[n]로 계산됨
int diff = i - 2 * prefix[i] + prefix[n];

 */