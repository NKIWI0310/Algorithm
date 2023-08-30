class Solution {
    public long minimumReplacement(int[] nums) {
        int n = nums.length;       // 배열의 길이
        int prev = nums[n-1];      // 이전 원소 (끝에서부터 시작)
        long ans = 0;              // 필요한 연산의 횟수
        
        // 끝에서부터 배열의 원소를 확인
        for (int i = n-2; i >= 0; i--) {
            // 현재 원소를 이전 원소로 몇 번 나눌 수 있는지 계산
            int noOfTime = nums[i] / prev;
            
            // 나머지가 있을 경우, 원소를 분할해야 함
            if (nums[i] % prev != 0) {
                noOfTime++;
                prev = nums[i] / noOfTime;
            }   
            
            // 연산 횟수를 누적
            ans += noOfTime - 1;
        }
        
        return ans;    // 최종 결과 반환
    }	
}
