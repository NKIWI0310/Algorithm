class Solution {
    public int maxScore(int[] nums) {
        Arrays.sort(nums);

        long sum = nums[nums.length-1];
        int count = 0;

        if(sum > 0)
            count++;
        else
            return 0;
        
        for(int i = nums.length-2 ; i >= 0; i--){
            sum += nums[i];
            if(sum > 0){
                count++;
            }
        }
        return count;
    }
}