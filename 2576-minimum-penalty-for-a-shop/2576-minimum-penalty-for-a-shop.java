class Solution {
    public int bestClosingTime(String customers) {
        int n = customers.length();

        int[] prefix = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + (customers.charAt(i - 1) == 'N' ? 0 : 1);
        }

        int minDiff = prefix[n]; // 첫 번째 차이는 모두 'N'일 때의 차이입니다.
        int bestClosingTime = 0;

        for (int i = 1; i <= n; i++) {
            // 'Y'로 시작하는 문자열의 경우 'Y'의 갯수에 대한 차이와 'N'의 갯수에 대한 차이를 계산합니다.
            int diff = i - 2 * prefix[i] + prefix[n];

            if (diff < minDiff) {
                minDiff = diff;
                bestClosingTime = i;
            }
        }
        return bestClosingTime;
    }
}
